from rest_framework import status
from rest_framework.test import APITestCase


class UsersAPITestCase(APITestCase):
    """ Тестирование API приложения пользователей """

    def setUp(self) -> None:
        """ Установка данных """

        self.user_data_list = [
            {
                "first_name": "Test",
                "last_name": "Testov",
                "email": "test.testov@mail.ru",
                "password": "123qwe456rty",
                "passwordConfirm": "123qwe456rty"
            },
            {
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "email": "ivan.ivanov@mail.ru",
                "password": "123qwe456rty",
                "passwordConfirm": "123qwe456rty"
            },
            {
                "first_name": "Petr",
                "last_name": "Petrov",
                "email": "petr.petrov@mail.ru",
                "password": "123qwe456rty",
                "passwordConfirm": "123qwe456rty"
            },
        ]

        self.login_data = {
            "email": "test.testov@mail.ru",
            "password": "123qwe456rty"
        }

    def test_users(self):
        """ Тестирование пользователя """

        # Test users registration
        for user_data in self.user_data_list:
            response = self.client.post('/api/users/registration/', data=user_data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            verification_token = response.json()['token']

            response = self.client.get(f'/api/users/verification/{verification_token}')

            self.assertRedirects(response, f'/api/users/verification/{verification_token}/', status_code=301)

        # Test user login
        response = self.client.post('/api/users/login/', data=self.login_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.json()['access']

        header = {"Authorization": f"Bearer {token}"}

        # Test getting user list
        response = self.client.get('/api/users/', headers=header)

        users = response.json()

        self.assertEqual(len(users), 3)

        # Test getting one user
        user_pk = 3

        response = self.client.get(f'/api/users/{user_pk}/', headers=header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = response.json()

        self.assertEqual(user['email'], 'petr.petrov@mail.ru')

        # Test update user
        patch_data = {"first_name": "Sidr"}

        response = self.client.patch(f'/api/users/edit/{user_pk}/', data=patch_data, headers=header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = response.json()

        self.assertEqual(user['first_name'], 'Sidr')

        # Test delete user
        response = self.client.delete(f'/api/users/delete/{user_pk}/', headers=header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
