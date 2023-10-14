from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from feedback.mixins import LikeDislikeMixin, FavoriteMixin, RatingMixin
from feedback.models import FavoriteFilm, Rating, Like
from feedback.permissions import IsFavoriteOwner
from feedback.serializers import FavoriteSerializer, RatingSerializer, LikeSerializer


class LikeAPIView(mixins.ListModelMixin, LikeDislikeMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class FavoriteAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, FavoriteMixin, GenericViewSet):
    queryset = FavoriteFilm.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class RatingAPIView(mixins.ListModelMixin, mixins.DestroyModelMixin, RatingMixin, GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset