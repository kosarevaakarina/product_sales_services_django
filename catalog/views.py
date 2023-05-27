from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Product, Contact


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


class ProductCreateView(generic.CreateView):
    model = Product
    extra_context = {
        "title": "Внести новый товар"
    }
    fields = ('name', 'description', 'image', 'category', 'price', 'created_date', 'changed_date')
    success_url = reverse_lazy('catalog:catalog')



