from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ('login', 'password', 'password2', 'secret_word')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    secret_word = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        login = attrs.get('login')
        secret_word = attrs.get('secret_word')
        new_password = attrs.get('new_password')

        if not User.objects.filter(login=login).exists():
            raise serializers.ValidationError('Пользователь с таким логином не существует!')

        user = User.objects.get(login=login)
        if user.secret_word != secret_word:
            raise serializers.ValidationError('Не правильное секретное слово')

        if len(new_password) < 3:
            raise serializers.ValidationError("Пароль должен быть от 3 и выше символов ")

        return attrs