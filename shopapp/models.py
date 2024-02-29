from django.db import models
from django.core import validators

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
