from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_user, get_user


class ProductsAPITestCase(APITestCase):
    """ Тестирование API основного приложения """

    def setUp(self) -> None:
        """ Установка данных """
        self.user = create_user()

        self.category_data_list = [
            {"name": "Телефоны"},
            {"name": "Ноутбуки"},
            {"name": "Планшеты"}
        ]

        self.product_data_list = [
            {"name": "Xiaomi Redmi Note 12", "amount": 15000},
            {"name": "Xiaomi Redmibook 15", "amount": 70000},
            {"name": "Xiaomi Redmi Pad Pro", "amount": 30000}
        ]

        user_login_data = {"email": "test.testov@mail.ru", "password": "123qwe456rty"}

        response = self.client.post('/api/users/login/', data=user_login_data)

        self.token = response.json()['access']

        self.header = {"Authorization": f"Bearer {self.token}"}

    def test_category_and_product(self):
        """ Тестирование создания и чтения всех категорий """

        # Test category creation
        for category_data in self.category_data_list:
            response = self.client.post('/api/category/create/', data=category_data, headers=self.header)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test category list
        response = self.client.get('/api/category/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        category_list = response.json()

        self.assertEqual(len(category_list), 3)

        # Test product creation
        user = get_user()

        category_pk = 1

        for raw_product_data in self.product_data_list:
            product_data = {
                "name": raw_product_data.get('name'),
                "category": category_pk,
                "amount": raw_product_data.get('amount'),
                "is_published": True,
                "user": user.pk
            }

            response = self.client.post('/api/products/create/', data=product_data, headers=self.header)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            category_pk += 1

        # Test getting products from one category
        for num in range(1, len(self.category_data_list) + 1):
            response = self.client.get(f'/api/category/{num}/products/', headers=self.header)

            product_name = response.json()[0]['name']

            product_data_name = self.product_data_list[num - 1]['name']

            self.assertEqual(product_name, product_data_name)

        # Test getting product list
        response = self.client.get(f'/api/products/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_list = response.json()

        self.assertEqual(len(product_list), 3)

        # Test getting one product
        product_pk = 1

        response = self.client.get(f'/api/products/{product_pk}/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = response.json()

        self.assertEqual(product['name'], 'Xiaomi Redmi Note 12')

        # Test update product
        patch_data = {"content": "Good phone for your usage!"}

        response = self.client.patch(f'/api/products/edit/{product_pk}/', data=patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_product = response.json()

        self.assertEqual(updated_product['content'], 'Good phone for your usage!')

        # Test delete product
        response = self.client.delete(f'/api/products/delete/{product_pk}/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
