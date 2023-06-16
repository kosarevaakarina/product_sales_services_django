from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version


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

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()


class ProductCreateView(generic.CreateView):
    model = Product
    extra_context = {
        "title": "Внести новый товар"
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form_with_formset.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)

        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:catalog')
