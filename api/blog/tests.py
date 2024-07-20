from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_user


class BlogAPITestCase(APITestCase):
    """ Тестирование API для блога """
    def setUp(self) -> None:
        """ Установка данных """
        self.user = create_user()

        self.blog_data_list = [
            {
                "title": "Test title",
                "body": "This is new test body for test title!"
            },
            {
                "title": "Test title1",
                "body": "This is new test body1 for test title1!"
            },
            {
                "title": "Test title2",
                "body": "This is new test body2 for test title2!"
            }
        ]

        user_login_data = {"email": "test.testov@mail.ru", "password": "123qwe456rty"}

        response = self.client.post('/api/users/login/', data=user_login_data)

        self.token = response.json()['access']

        self.header = {"Authorization": f"Bearer {self.token}"}

    def test_blog(self):
        """ Тестирование блога """

        # Test blogs creation
        for blog_data in self.blog_data_list:
            response = self.client.post('/api/blog/create/', data=blog_data, headers=self.header)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test getting blog list
        response = self.client.get('/api/blog/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        blogs = response.json()

        self.assertEqual(len(blogs), 3)

        # Test getting one blog
        blog_pk = 2

        response = self.client.get(f'/api/blog/{blog_pk}/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        blog = response.json()

        self.assertEqual(blog['title'], 'Test title1')

        # Test blog update
        patch_data = {"body": "This is new test body4 for test title4!"}

        response = self.client.patch(f'/api/blog/edit/{blog_pk}/', data=patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        blog = response.json()

        self.assertEqual(blog['body'], 'This is new test body4 for test title4!')

        # Test blog delete
        response = self.client.delete(f'/api/blog/delete/{blog_pk}/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
