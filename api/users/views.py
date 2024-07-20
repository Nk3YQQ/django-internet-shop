from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView as BaseTokenObtainPairView,
                                            TokenRefreshView as BaseTokenRefreshView)

from users.models import User, EmailRegistrationToken
from api.users.serializers import UsersSerializer, UsersRegistrationSerializer
from users.services import send_message_for_activation


@extend_schema_view(
    post=extend_schema(description='Controller for refresh token', tags=['Auth'], operation_id='refresh_token')
)
class TokenRefreshView(BaseTokenRefreshView):
    """ Refresh токен """
    pass


@extend_schema_view(
    post=extend_schema(description='Controller for access token', tags=['Auth'], operation_id='access_token')
)
class TokenObtainPairView(BaseTokenObtainPairView):
    """ Токен аутентификации """
    pass


@extend_schema_view(
    post=extend_schema(description='Create a new user', tags=['Users'], operation_id='user_create')
)
class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """
    serializer_class = UsersRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        token = EmailRegistrationToken.objects.create(user=user)

        send_message_for_activation(self.request, token.token, user.email)

    def create(self, request, *args, **kwargs):
        instance = super().create(request, *args, **kwargs)

        email = instance.data['email']

        user = User.objects.get(email=email)

        token = EmailRegistrationToken.objects.get(user=user)

        return Response(
            {'message': 'Для подтверждения регистрации профиля, проверьте электронную почту',
             "token": token.token},
            status=status.HTTP_201_CREATED
        )


@extend_schema_view(
    get=extend_schema(description='Get users list', tags=['Users'], operation_id='user_list')
)
class UserListAPIView(generics.ListAPIView):
    """ Чтение всех пользователей """
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    get=extend_schema(description='Get one user', tags=['Users'], operation_id='user_retrieve')
)
class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного пользователя """
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    put=extend_schema(description='Update user', tags=['Users'], operation_id='user_update'),
    patch=extend_schema(description='Update user particular', tags=['Users'], operation_id='user_update_particular')
)
class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление пользователя """
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    delete=extend_schema(description='Delete user', tags=['Users'], operation_id='user_delete')
)
class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    get=extend_schema(description='Verify user email', tags=['Users'], operation_id='verify')
)
class VerifyEmailAPIView(APIView):
    """ Подтверждение почты пользователя """
    @staticmethod
    def get(request, token):
        try:
            token = EmailRegistrationToken.objects.get(token=token)
            user = token.user
            user.is_active = True
            user.save()
            token.delete()
            return Response({'message': 'Аккаунт успешно подтверждён!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'Неверный токен!'}, status=status.HTTP_400_BAD_REQUEST)
