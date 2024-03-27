from django.urls import path

from blogapp.views import UserMaterialListView
from shopapp.views import UserProducts
from users.apps import UsersConfig
from users.views import UserRegistration, LoginView, LogoutView, UserDetailView, UserUpdateView, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('edit/', UserUpdateView.as_view(), name='edit'),
    path('respassword/', reset_password, name='respassword'),
    path('products/', UserProducts.as_view(), name='user_products'),
    path('materials/', UserMaterialListView.as_view(), name='user_materials')
]
