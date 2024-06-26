from django.test import TestCase

from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name='Test', last_name='Testov', email='test.testov@mail.ru')

    def test_user(self):
        user = User.objects.get(email='test.testov@mail.ru')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'Testov')
        self.assertEqual(user.email, 'test.testov@mail.ru')
