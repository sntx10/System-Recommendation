from django.urls import include, path
from rest_framework.routers import DefaultRouter

from feedback.views import LikeAPIView, RatingAPIView, FavoriteAPIView

router = DefaultRouter()
router.register('like', LikeAPIView)
router.register('rating', RatingAPIView)
router.register('favourite', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls))
]