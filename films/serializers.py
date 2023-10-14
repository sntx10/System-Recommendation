from django.db.models import Avg
from rest_framework import serializers

from feedback.models import Rating, Like
from films.models import Film, Tag
from django.contrib.auth import get_user_model

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']


class FilmSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['likes'] = Like.objects.filter(film=instance, like=True).count()
        rating = Rating.objects.filter(film=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            res['rating'] = rating
        else:
            res['rating'] = 0
        return res

    class Meta:
        model = Film
        fields = ['id', 'image', 'title', 'tags', 'release_year', 'description']