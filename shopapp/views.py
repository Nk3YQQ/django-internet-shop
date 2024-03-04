from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from shopapp.models import Category, Product
from .forms import ProductForm


class BaseProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("query")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ProductListView(BaseProductListView):
    pass


class ProductCategoryListView(BaseProductListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class CategoryListView(ListView):
    model = Category


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shopapp:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Category.objects.all()
        return context
