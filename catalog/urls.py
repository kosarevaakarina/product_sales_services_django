from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import BlogListView, ContactCreateView, ProductsListView, ProductDetailView, ProductCreateView, \
    BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView, count_of_view

app_name = CatalogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('catalog/', ProductsListView.as_view(), name='catalog'),
    path('product_items/<int:pk>/', ProductDetailView.as_view(), name='product_items'),
    path('product/create/', ProductCreateView.as_view(), name='save_product'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/form/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_confirm_delete'),
    path('blog/count/<int:pk>/', count_of_view, name='count_of_view')

]
