# Generated by Django 5.0.2 on 2024-02-28 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_alter_product_content_squashed_0005_alter_product_amount_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Товар не может стоить меньше 1 рубля')], verbose_name='Цена за покупку'),
        ),
    ]