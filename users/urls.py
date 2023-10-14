from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', ChangePasswordView.as_view()),


]