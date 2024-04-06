from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/media/shopapp/not_found.jpeg'


@register.filter()
def edit_or_create_button(obj):
    if obj:
        return 'Сохранить'
    return 'Создать'


@register.filter()
def edit_or_create_good(obj):
    if obj:
        return 'Редактирование товара'
    return 'Заполните поля для того, чтобы добавить товар'


@register.filter()
def check_version(obj):
    if obj:
        return f'Название версии: {obj}'
    return 'Название версии: -'


@register.filter()
def check_content(obj):
    if obj:
        return obj[:100]
    return 'Отсутствует'


@register.filter()
def check_owner(obj):
    if obj:
        return obj
    return 'Отсутствует'


@register.filter()
def is_moderator(user):
    moderator_group = Group.objects.get(name='Модератор')
    return moderator_group in user.groups.all()
