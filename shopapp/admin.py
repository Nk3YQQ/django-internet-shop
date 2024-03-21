from django.contrib import admin

from shopapp.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image', 'amount',)
    list_filter = ('amount', 'category')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'product')
