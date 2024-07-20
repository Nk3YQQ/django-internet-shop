from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Category, Product, Version
from .forms import ProductForm, VersionForm
from .services import get_cache_for_product_detail, get_cache_for_category


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


class CategoryProductListView(BaseProductListView):
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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        object_list = get_cache_for_category(self.get_queryset())

        context_data['object_list'] = object_list

        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product = get_cache_for_product_detail(self.object, self.object.pk)

        context_data['object'] = product

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('users:user_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category_list'] = Category.objects.all()

        return context

    def form_valid(self, form):
        instance = form.save()

        instance.user = self.request.user

        instance.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'products.change_product'

    def get_object(self, queryset=None):
        instance = super().get_object(queryset)

        if instance.user != self.request.user and not self.request.user.is_staff:
            return HttpResponseForbidden("You do not have permission to access this resource.")

        return instance

    def get_success_url(self):
        return reverse('products:product_edit', args=[self.kwargs.get('pk')])

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

        instance = form.save()

        if formset.is_valid():
            formset.instance = instance

            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get_object(self, queryset=None):
        instance = super().get_object(queryset)

        if instance.user != self.request.user:
            return HttpResponseForbidden("You do not have permission to access this resource.")

        return instance


@login_required
def toggle_material(request, pk):
    material = get_object_or_404(Product, pk=pk)

    if material.is_published:
        material.is_published = False

    else:
        material.is_published = True

    material.save()

    return redirect(reverse('products:product_list'))
