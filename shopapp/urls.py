from django.urls import path

from shopapp.apps import ShopappConfig
from shopapp.views import categories, get_good, index, get_category, add_product

app_name = ShopappConfig.name

urlpatterns = [
    path('', index, name='main'),
    path('categories/', categories, name='all_categories'),
    path('goods/<int:pk>/', get_good, name='one_good'),
    path('category/<int:pk>/', get_category, name='one_category'),
    path('add/', add_product, name='add_product')
]

