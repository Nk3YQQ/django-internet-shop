from django import forms

from config.settings import FORBIDDEN_WORDS
from .models import Product, Version


def check_words(clean_data, forbidden_words, verbose_name):
    if clean_data.lower() in forbidden_words:
        raise forms.ValidationError(f"В поле '{verbose_name}' обнаружено запрещённое слово")


class ProductForm(forms.ModelForm):
    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        verbose_name = self.fields.get('name').label
        check_words(clean_data, FORBIDDEN_WORDS, verbose_name)
        return clean_data

    def clean_content(self):
        clean_data = self.cleaned_data.get('content')
        verbose_name = self.fields.get('content').label
        check_words(clean_data, FORBIDDEN_WORDS, verbose_name)
        return clean_data

    class Meta:
        model = Product
        fields = ('name', 'content', 'category', 'image', 'amount',)


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
