from django.contrib import admin

from blogapp.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'created_at', 'is_published', 'view_count')
    list_filter = ('is_published', 'view_count')
