from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import ProductForm, VersionForm, ProductFormCutted
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


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    extra_context = {
        "title": "Внести новый товар"
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateCuttedView(PermissionRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductFormCutted
    permission_required = 'catalog.can_edit_description_and_category_product'

    def get_success_url(self):
        return reverse('catalog:product_items', kwargs={'pk': self.object.pk})


class ProductUpdateView(generic.UpdateView):
    model = Product
    template_name = 'catalog/product_form_with_formset.html'
    form_class = ProductForm

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
        return reverse('catalog:product_items', kwargs={'pk': self.object.pk})


@permission_required('catalog.set_published_product')
def change_is_published(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    product_item.toggle_is_published()
    return redirect(reverse('catalog:product_items', args=[product_item.pk]))
