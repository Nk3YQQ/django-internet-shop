from django.urls import path

from blogapp.apps import BlogappConfig
from blogapp.views import (MaterialListView, MaterialDetailView, MaterialCreateView, MaterialUpdateView,
                           MaterialDeleteView, toggle_material)

app_name = BlogappConfig.name

urlpatterns = [
    path('', MaterialListView.as_view(), name='main'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='one_material'),
    path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit_material'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete_material'),
    path('add/', MaterialCreateView.as_view(), name='add_material'),
    path('activity/<int:pk>/', toggle_material, name='toggle_material')
]
