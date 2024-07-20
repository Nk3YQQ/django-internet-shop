from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsModerator, IsOwner
from api.shopapp.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product


@extend_schema_view(
    post=extend_schema(description='Create a new category', tags=['Categories'], operation_id='category_create')
)
class CategoryCreateAPIView(generics.CreateAPIView):
    """ Создание категории """
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    get=extend_schema(description='Read all categories', tags=['Categories'], operation_id='category_list')
)
class CategoryListAPIView(generics.ListAPIView):
    """ Чтение всех категорий """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    post=extend_schema(description='Create a new product', tags=['Products'], operation_id='product_create')
)
class ProductCreateAPIView(generics.CreateAPIView):
    """ Создание товара """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductBaseListAPIView(generics.ListAPIView):
    """ Базовый класс для списка продуктов """
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


@extend_schema_view(
    get=extend_schema(description='Read all products', tags=['Products'], operation_id='product_list')
)
class ProductListAPIView(ProductBaseListAPIView):
    """ Чтение всех продуктов """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@extend_schema_view(
    get=extend_schema(
        description='Read products from category',
        tags=['Products'],
        operation_id='category_product_list'
    )
)
class CategoryProductListView(ProductBaseListAPIView):
    """ Чтение товаров из одной категории """
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        category = Category.objects.get(pk=category_id)
        return Product.objects.filter(category=category)


@extend_schema_view(
    get=extend_schema(description='Read one product', tags=['Products'], operation_id='product_retrieve')
)
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного товара """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


@extend_schema_view(
    put=extend_schema(description='Update product', tags=['Products'], operation_id='product_update'),
    patch=extend_schema(
        description='Update product particular',
        tags=['Products'],
        operation_id='product_update_particular'
    )
)
class ProductUpdateAPIView(generics.UpdateAPIView):
    """ Обновление товара """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


@extend_schema_view(
    delete=extend_schema(description='Delete product', tags=['Products'], operation_id='product_delete')
)
class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Удаление товара """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
