from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        permission_classes = [IsAuthenticated]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        permission_classes = [IsAuthenticated]
