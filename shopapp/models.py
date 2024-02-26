from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    content = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, verbose_name='Категория')
    amount = models.IntegerField(verbose_name='Цена за покупку')
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
    content = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
