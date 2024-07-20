from django.urls import path

from api.blog.views import BlogCreateAPIView, BlogListAPIView, BlogRetrieveAPIView, BlogUpdateAPIView, \
    BlogDestroyAPIView

urlpatterns = [
    path('create/', BlogCreateAPIView.as_view(), name='blog_create'),
    path('', BlogListAPIView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogRetrieveAPIView.as_view(), name='blog_retrieve'),
    path('edit/<int:pk>/', BlogUpdateAPIView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDestroyAPIView.as_view(), name='blog_delete')
]
