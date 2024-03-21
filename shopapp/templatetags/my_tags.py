from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/media/shopapp/not_found.jpeg'


@register.filter()
def edit_or_create_button(obj):
    if obj:
        return 'Редактировать'
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
