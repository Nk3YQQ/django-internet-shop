from django.urls import path

from api.products.views import (ProductCreateAPIView, CategoryListAPIView, ProductRetrieveAPIView,
                                CategoryProductListView, ProductListAPIView, ProductUpdateAPIView, ProductDestroyAPIView,
                                CategoryCreateAPIView)

urlpatterns = [
    # Categories
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/products/', CategoryProductListView.as_view(), name='category_product_list'),

    # Products
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('products/edit/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete')
]
