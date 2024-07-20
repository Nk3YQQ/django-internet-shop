from django.urls import path

from blog.views import UserBlogListView
from products.views import UserProducts
from users.apps import UsersConfig
from users.views import UserRegistration, LoginView, LogoutView, UserDetailView, UserUpdateView, reset_password, \
    registration_done, ActivateAccountView

app_name = UsersConfig.name

urlpatterns = [
    # Auth
    path('registration/', UserRegistration.as_view(), name='register'),
    path('registration/done/', registration_done, name='registration_done'),
    path('registration/activate/<uuid:token>', ActivateAccountView.as_view(), name='registration_activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Users
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('edit/', UserUpdateView.as_view(), name='user_edit'),
    path('reset/', reset_password, name='reset_password'),
    path('products/', UserProducts.as_view(), name='user_products'),
    path('blog/', UserBlogListView.as_view(), name='user_blog')
]
