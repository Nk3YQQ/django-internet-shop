from django.test import TestCase

from blogapp.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title='Название', body='Содержимое')

    def test_blog(self):
        blog = Blog.objects.get(title='Название')
        self.assertEqual(blog.body, 'Содержимое')
        self.assertEqual(blog.is_published, True)
