from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.models import Product, Contact, Blog


class ProductsListView(generic.ListView):
    model = Product
    extra_context = {
        "title": "Каталог товаров"
    }


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['product']
        return context_data


class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('name', 'phone', 'message')
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'created_date', 'changed_date')
    success_url = reverse_lazy('catalog:catalog')


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {
        "title": "Новости дня"
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'create_date')
    success_url = reverse_lazy('catalog:home')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'create_date')
    success_url = reverse_lazy('catalog:home')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:home')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


def count_of_view(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    blog_item.count_of_view += 1
    blog_item.save()
    return redirect(reverse('catalog:home'))
