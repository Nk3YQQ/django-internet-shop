from django import template

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
