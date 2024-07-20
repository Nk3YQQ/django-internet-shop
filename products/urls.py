from django.shortcuts import redirect
from django.urls import path, reverse
from django.views.decorators.cache import cache_page

from products.apps import ProductsConfig
from products.views import (CategoryListView, ProductDetailView, ProductListView, CategoryProductListView,
                            ProductCreateView, ProductUpdateView, toggle_material)

app_name = ProductsConfig.name

urlpatterns = [
    # Main
    path('', lambda request: redirect(reverse('products:product_list')), name='main'),

    # Categories
    path('category/', cache_page(60)(CategoryListView.as_view()), name='category_list'),
    path('category/<int:pk>/products/', CategoryProductListView.as_view(), name='category_product_list'),

    # Products
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_retrieve'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('activity/<int:pk>/', toggle_material, name='toggle_material')
]
