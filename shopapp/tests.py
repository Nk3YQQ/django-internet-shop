from django.test import TestCase

from shopapp.models import Product, Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Планшеты')
        Category.objects.create(name='Телефоны')

    def test_category_list(self):
        categories_count = Category.objects.count()
        self.assertEqual(categories_count, 2)


class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Ноутбуки')

        Product.objects.create(name='Xiaomi Redmibook 15', category=category, amount=50000)

    def test_get_product(self):
        product = Product.objects.get(name='Xiaomi Redmibook 15')

        self.assertEqual(product.category.name, 'Ноутбуки')

    def test_update_product(self):
        product = Product.objects.get(name='Xiaomi Redmibook 15')

        product.name = 'Xiaomi Redmi 8 Pro'

        self.assertEqual(product.name, 'Xiaomi Redmi 8 Pro')
