from django.test import TestCase

from shopapp.models import Product, Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Планшеты')
        Category.objects.create(name='Телефоны')

    def test_category(self):
        categories_count = Category.objects.count()
        self.assertEquals(categories_count, 2)


class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Ноутбуки')

        Product.objects.create(name='Xiaomi Redmibook 15', category=category, amount=50000)

    def test_product(self):
        product = Product.objects.get(name='Xiaomi Redmibook 15')

        self.assertEqual(product.category, 'Ноутбуки')
