from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shopapp.models import Category, Product, Version
from .forms import ProductForm, VersionForm


class BaseProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        name = self.request.GET.get("query")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        hidden_objects = Product.objects.filter(is_published=False)

        context_data['user'] = self.request.user
        context_data['hidden_objects'] = hidden_objects

        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(is_current_version=True).first()

        return context_data


class ProductListView(BaseProductListView):
    pass


class ProductCategoryListView(BaseProductListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class UserProducts(BaseProductListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user)
        return queryset


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('users:user_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'shopapp.change_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('shopapp:product_edit', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


@login_required
def toggle_material(request, pk):
    material = get_object_or_404(Product, pk=pk)
    if material.is_published:
        material.is_published = False
    else:
        material.is_published = True

    material.save()
    return redirect(reverse('shopapp:main'))
