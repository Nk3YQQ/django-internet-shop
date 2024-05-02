from django.test import TestCase

from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name='Test', last_name='Testov', email='test.testov@mail.ru')

    def test_user(self):
        user = User.objects.get(email='test.testov@mail.ru')
        self.assertEquals(user.first_name, 'Test')
        self.assertEquals(user.last_name, 'Testov')
        self.assertEquals(user.email, 'test.testov@mail.ru')
