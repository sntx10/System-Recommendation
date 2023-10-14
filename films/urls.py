from django.urls import path, include
from rest_framework.routers import DefaultRouter

from films.views import FilmViewSet, RecommendationView

router = DefaultRouter()
router.register('', FilmViewSet)


urlpatterns = [
    path('recommended/', RecommendationView.as_view()),
    path('', include(router.urls)),
]