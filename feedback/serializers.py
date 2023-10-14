from rest_framework import serializers

from feedback.models import Like, FavoriteFilm, Rating


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['film'] = instance.film.title
        return res


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteFilm
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username
        rep['film'] = instance.film.title
        return rep


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)
    film = serializers.CharField(required=False)

    class Meta:
        model = Rating
        fields = ['rating', 'film']