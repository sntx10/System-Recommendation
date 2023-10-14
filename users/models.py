from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, login, **extra_fields):
        user = self.model(login=login, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, login, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(password, login, **extra_fields)

    def create_superuser(self, password, login, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(password, login, **extra_fields)


class CustomUser(AbstractUser):
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    login = models.CharField(max_length=50, unique=True)
    username = None
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    secret_word = models.CharField(max_length=100)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.login}'