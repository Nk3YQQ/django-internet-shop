from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.blog.serializers import BlogSerializer
from blog.models import Blog


@extend_schema_view(
    post=extend_schema(description='Create a new blog', tags=['Blog'], operation_id='blog_create')
)
class BlogCreateAPIView(generics.CreateAPIView):
    """ Создание блога """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    get=extend_schema(description='Reading all blogs', tags=['Blog'], operation_id='blog_list')
)
class BlogListAPIView(generics.ListAPIView):
    """ Чтение всех блогов """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    get=extend_schema(description='Reading one blog', tags=['Blog'], operation_id='blog_retrieve')
)
class BlogRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного блога """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    put=extend_schema(description='Update blog', tags=['Blog'], operation_id='blog_update'),
    patch=extend_schema(description='Update blog particular', tags=['Blog'], operation_id='blog_update_particular')
)
class BlogUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование блога """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    delete=extend_schema(description='Delete blog', tags=['Blog'], operation_id='blog_delete')
)
class BlogDestroyAPIView(generics.DestroyAPIView):
    """ Удаление блога """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]
