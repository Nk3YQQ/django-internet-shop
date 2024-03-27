from django import template

register = template.Library()


@register.filter()
def login_or_register(val):
    if val == 'register':
        return 'Зарегистрироваться'
    return 'Войти'


@register.filter()
def login_or_register_header(val):
    if val == 'register':
        return 'Регистрация'
    return 'Вход в аккаунт'


@register.filter()
def profile_or_edit(val):
    if val == 'edit':
        return 'Редактирование'
    return 'Информация о пользователе'
