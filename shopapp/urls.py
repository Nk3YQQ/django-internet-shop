from django.urls import path

from shopapp.views import categories, get_good, get_all_goods, index, get_category, add_product

urlpatterns = [
    path('', index, name='main'),
    path('categories/', categories, name='all_categories'),
    path('goods/<int:pk>/', get_good, name='one_good'),
    path('goods/', get_all_goods, name='all_goods'),
    path('goods', get_category, name='one_category'),
    path('add/', add_product, name='add_product')
]

