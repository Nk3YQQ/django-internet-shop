from django.urls import path

from api.users.views import (UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView,
                             UserDestroyAPIView, TokenObtainPairView, TokenRefreshView, VerifyEmailAPIView)

urlpatterns = [
    # Auth
    path('registration/', UserCreateAPIView.as_view(), name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('verification/<uuid:token>/', VerifyEmailAPIView.as_view(), name='verification'),

    # Users
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('edit/<int:pk>/', UserUpdateAPIView.as_view(), name='user_edit'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # Refresh Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
