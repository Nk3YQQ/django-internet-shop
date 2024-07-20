import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User, EmailRegistrationToken
from users.services import send_message_for_activation


class UserRegistration(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:registration_done')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['intent'] = 'register'
        return context_data

    def form_valid(self, form):
        user = form.save()

        if form.is_valid():
            user.is_active = False

            token = EmailRegistrationToken.objects.create(user=user)

            send_message_for_activation(self.request, token.token, user.email)

        return super().form_valid(form)


def registration_done(request):
    return render(request, 'users/registration_done.html')


class ActivateAccountView(View):
    """ Активирует аккаунт пользователя """

    @staticmethod
    def get(request, token):
        try:
            token_obj = EmailRegistrationToken.objects.get(token=token)
        except ObjectDoesNotExist:
            token_obj = None

        if token_obj:
            user = token_obj.user
            user.is_active = True
            user.save()
            token_obj.delete()
            return render(request, 'users/activation_complete.html', status=200)
        else:
            return render(request, 'users/activation_invalid.html', status=400)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['intent'] = 'login'
        return context_data


class LogoutView(BaseLogoutView):
    pass


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['intent'] = 'profile'
        return context_data


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['intent'] = 'edit'
        return context_data


def reset_password(request):
    new_password = ''.join([str(random.randint(1, 9)) for _ in range(15)])
    send_mail(
        subject='Смена пароля!',
        message=f'Ваш временный пароль: {new_password}. Поторопитесь изменить его!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('products:main'))
