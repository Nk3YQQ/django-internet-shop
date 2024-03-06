from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blogapp.models import Blog


class MaterialListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        print(self.object.preview)
        self.object.view_count += 1
        if self.object.view_count == 100:
            send_mail('Поздравляем со 100 просмотрами!',
                      f'Ваше объявление "{self.object.title}" достигло 100 просмотров!',
                      'skypro.test.testov@yandex.ru',
                      ['nkirishima@mail.ru'],
                      fail_silently=False
                      )
        self.object.save()
        return self.object


class MaterialCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blogapp:main')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview')

    def get_success_url(self):
        return reverse('blogapp:one_material', args=[self.kwargs.get('pk')])


class MaterialDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogapp:main')


def toggle_material(request, pk):
    material = get_object_or_404(Blog, pk=pk)
    if material.is_published:
        material.is_published = False
    else:
        material.is_published = True

    material.save()
    return redirect(reverse('blogapp:main'))
