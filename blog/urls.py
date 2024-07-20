from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView,
                        BlogDeleteView, toggle_material)

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_retrieve'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity/<int:pk>/', toggle_material, name='toggle_material')
]
