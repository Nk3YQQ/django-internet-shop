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
        product_1 = Product.objects.get(name='Xiaomi Redmibook 15')
        product_2 = Product.objects.get(name='Xiaomi Redmi Note 8')
        product_3 = Product.objects.get(name='Apple iPad Pro')

        self.assertEqual(product_1.category, 'Ноутбуки')
        self.assertEqual(product_2.category, 'Телефоны')
        self.assertEqual(product_3.category, 'Планшеты')
