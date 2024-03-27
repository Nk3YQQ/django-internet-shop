from django.db import models
from django.core import validators

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    content = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='shopapp/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, verbose_name='Категория')
    amount = models.IntegerField(
        verbose_name='Цена за покупку',
        validators=[validators.MinValueValidator(1, message='Товар не может стоить меньше 1 рубля')]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата последнего изменения')

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Продукт', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.amount}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-created_at',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', unique=True)
    image = models.ImageField(upload_to='shopapp/', verbose_name='Изображение', **NULLABLE)
    content = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    number = models.IntegerField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current_version = models.BooleanField(default=True, verbose_name='Является текущей версией?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
