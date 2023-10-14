from datetime import datetime, timedelta
from functools import reduce

from django.db.models import Q
import django_filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from feedback.models import Rating, FavoriteFilm
from films.models import Film, Tag
from films.serializers import FilmSerializer

User = get_user_model()


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100000


class FilmFilter(django_filters.FilterSet):
    tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(), field_name='tags')

    class Meta:
        model = Film
        fields = ['tags', 'release_year',]


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_class = FilmFilter
    pagination_class = LargeResultsSetPagination
    search_fields = ['tags__name', 'title']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

class RecommendationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        latest_ratings = Rating.objects.filter(user=user).order_by('-created_at')[:5]
        if len(latest_ratings) < 10:
            latest_ratings = Rating.objects.filter(user=user)

        tags = []
        for rating in latest_ratings:
            film = rating.film
            tags += film.tags.all()

        favorite_films = FavoriteFilm.objects.filter(user=user).values_list('film', flat=True)

        film_list = Film.objects.filter(reduce(lambda x, y: x | y, [Q(tags=tag) for tag in tags]))
        if favorite_films:
            film_list = film_list.filter(reduce(lambda x, y: x | y, [Q(tags=tag) for tag in favorite_films]))

        six_months_ago = datetime.now() - timedelta(days=180)
        film_list = film_list.filter(created_at__gte=six_months_ago)

        if len(film_list) < 10:
            serializer = FilmSerializer(film_list, many=True)
            return Response(serializer.data)

        film_list = sorted(film_list, key=lambda m: len(set(m.tags.all()) & set(tags)), reverse=True)
        recommend_films = film_list[:10]

        serializer = FilmSerializer(recommend_films, many=True)
        return Response(serializer.data)