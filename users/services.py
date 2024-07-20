from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string

from users.models import User


def send_message_for_activation(request, token, email):
    """ Функция отправляет сообщение для активации аккаунта пользователя по электронной почте """

    mail_subject = 'Активация аккаунта'

    domain = request.get_host()

    message = render_to_string('users/acc_active_email.html', {
        'domain': domain,
        'token': token
    })

    send_mail(
        subject=mail_subject,
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=message
    )


def create_user():
    User.objects.create(
        id=1,
        first_name='Test',
        last_name='Testov',
        email='test.testov@mail.ru',
        password=make_password('123qwe456rty')
    )


def get_user():
    return User.objects.get(email='test.testov@mail.ru')
