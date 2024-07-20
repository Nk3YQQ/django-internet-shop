from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from users.models import User


class UsersRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    passwordConfirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'passwordConfirm')
        permission_classes = [IsAuthenticated]

    def validate(self, attrs):
        password = attrs.get('password')
        passwordConfirm = attrs.get('passwordConfirm')

        if password != passwordConfirm:
            raise serializers.ValidationError('Пароли не совпадают')

        return attrs

    def create(self, validated_data):
        validated_data.pop('passwordConfirm')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email',)
