from django.urls import path
from django.views.decorators.cache import cache_page

from shopapp.apps import ShopappConfig
from shopapp.views import (CategoryListView, ProductDetailView, ProductListView, ProductCategoryListView,
                           ProductCreateView, ProductUpdateView, toggle_material)

app_name = ShopappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('categories/', cache_page(60)(CategoryListView.as_view()), name='all_categories'),
    path('goods/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='one_good'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='one_category'),
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('activity/<int:pk>/', toggle_material, name='toggle_material')
]
