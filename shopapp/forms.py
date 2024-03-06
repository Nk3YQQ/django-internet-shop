from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Название', max_length=50)
    content = forms.CharField(label='Описание', widget=forms.Textarea, required=False)
    image = forms.ImageField(label='Изображение', required=False)
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())
    amount = forms.IntegerField(label='Цена')

    class Meta:
        model = Product
        fields = ('name', 'content', 'category', 'image', 'amount',)
