from django.conf import settings
from django.core.cache import cache


def get_cache_for_product_detail(product, pk):
    if settings.CACHE_ENABLED:
        key = f'product_detail_{pk}'
        object_detail = cache.get(key)

        if object_detail is None:
            object_detail = product
            cache.set(key, object_detail)

    else:
        object_detail = product

    return object_detail


def get_cache_for_category(categories):
    if settings.CACHE_ENABLED:
        key = 'category_list'
        object_list = cache.get(key)

        if object_list is None:
            object_list = categories
            cache.set(key, object_list)

    else:
        object_list = categories

    return object_list
