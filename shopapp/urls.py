from django.urls import path

from shopapp.views import index

urlpatterns = [
    path('', index)
]

