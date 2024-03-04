from django.urls import path

from shopapp.apps import ShopappConfig
from shopapp.views import CategoryListView, ProductDetailView, ProductListView, ProductCategoryListView, ProductCreateView

app_name = ShopappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('categories/', CategoryListView.as_view(), name='all_categories'),
    path('goods/<int:pk>/', ProductDetailView.as_view(), name='one_good'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='one_category'),
    path('add/', ProductCreateView.as_view(), name='add_product')
]

