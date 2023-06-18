from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *


app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('catalog/', ProductsListView.as_view(), name='catalog'),
    path('product_items/<int:pk>/', ProductDetailView.as_view(), name='product_items'),
    path('product/create/', ProductCreateView.as_view(), name='save_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_form'),
    path('product/update_cutted/<int:pk>/', ProductUpdateCuttedView.as_view(), name='product_form_cutted'),
    path('product/is_published/<int:pk>/', change_is_published, name='change_is_published')
]
