from django.core.management import BaseCommand
from django.db import IntegrityError

from products.models import Category


class Command(BaseCommand):
    """ Команда создаёт 10 базовых категорий """

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Ноутбуки', 'image': 'products/laptops.png'},
            {'name': 'Телефоны', 'image': 'products/phones.png'},
            {'name': 'Планшеты', 'image': 'products/tablets.jpg'},
            {'name': 'Часы', 'image': 'products/watches.jpg'},
            {'name': 'Наушники', 'image': 'products/headphones.jpg'},
            {'name': 'Компьютеры', 'image': 'products/computers.jpg'},
            {'name': 'Мониторы', 'image': 'products/monitors.png'},
            {'name': 'Микроволновки', 'image': 'products/microwaves.jpg'},
            {'name': 'Телевизоры', 'image': 'products/tv.png'},
            {'name': 'Стиральные машины', 'image': 'products/washing-machine.jpg'},
        ]

        for category in category_list:
            try:
                Category.objects.create(**category)

            except IntegrityError:
                continue
