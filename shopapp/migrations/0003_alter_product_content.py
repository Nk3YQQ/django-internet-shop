# Generated by Django 5.0.2 on 2024-02-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_category_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]