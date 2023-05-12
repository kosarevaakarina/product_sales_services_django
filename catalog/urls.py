from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, catalog, product_items, save_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('product_items/<int:pk>/', product_items, name='product_items'),
    path('save_product/', save_product, name='save_product')
]