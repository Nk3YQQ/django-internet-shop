import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.IntegerField(verbose_name='Номер телефона', **NULLABLE)
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, verbose_name='Страна', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmailRegistrationToken(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.token} - {self.user}'

    class Meta:
        verbose_name = 'Токен подтверждения'
        verbose_name_plural = 'Токены подтверждения'
