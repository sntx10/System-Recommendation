from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    image = models.ImageField(upload_to='films')
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    release_year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} --> {"Release-year"} -- {self.release_year}'


class WatchedFilm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='views')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='views')
    date = models.DateTimeField(default=timezone.now)