from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, catalog, product_items

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('product_items/<int:pk>/', product_items, name='product_items')
]