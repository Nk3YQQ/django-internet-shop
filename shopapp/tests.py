from django.test import TestCase

from shopapp.models import Product, Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Ноутбуки')
        Category.objects.create(name='Телефоны')
        Category.objects.create(name='Планшеты')

    def test_category(self):
        categories_count = Category.objects.count()
        self.assertEquals(categories_count, 3)


class ProductTestCase(TestCase):
    def setUp(self):
        category_1 = Category.objects.get(name='Ноутбуки')
        category_2 = Category.objects.get(name='Телефоны')
        category_3 = Category.objects.get(name='Планшеты')

        Product.objects.create(name='Xiaomi Redmibook 15', category=category_1, amount=50000)
        Product.objects.create(name='Xiaomi Redmi Note 8', category=category_2, amount=10000)
        Product.objects.create(name='Apple iPad Pro', category=category_3, amount=100000)

    def test_product(self):
        product_1 = Product.objects.get(name='Xiaomi Redmibook 15')
        product_2 = Product.objects.get(name='Xiaomi Redmi Note 8')
        product_3 = Product.objects.get(name='Apple iPad Pro')

        self.assertEqual(product_1.category, 'Ноутбуки')
        self.assertEqual(product_2.category, 'Телефоны')
        self.assertEqual(product_3.category, 'Планшеты')
