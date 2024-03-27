import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class UserRegistration(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['intent'] = 'register'
        return context_data

    def form_valid(self, form):
        new_user = form.save()
        if form.is_valid():
            send_mail(
                subject='Добро пожаловать на сайт!',
                message=f'Приветствую Вас! Вы зарегистрировались на сайте E&I Company. Здесь вы можете найти любую '
                        f'технику для работы на вкус',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email],
            )
        return super().form_valid(form)


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
    return redirect(reverse('shopapp:main'))
