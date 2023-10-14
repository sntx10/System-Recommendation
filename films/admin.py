from django.contrib import admin

from feedback.models import FavoriteFilm, Like, Rating
from films.models import Film, Tag, WatchedFilm

# Register your models here.

admin.site.register(Film)
admin.site.register(Like)
admin.site.register(FavoriteFilm)
admin.site.register(Tag)
admin.site.register(WatchedFilm)
admin.site.register(Rating)