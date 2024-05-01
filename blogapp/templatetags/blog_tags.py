from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/media/shopapp/not_found.jpeg'


@register.filter()
def save_or_edit(val):
    if val:
        return 'Сохранить'
    return 'Создать'


@register.filter()
def is_content_manager(user):
    moderator_group = Group.objects.get(name='Контент-менеджер')
    return moderator_group in user.groups.all()
