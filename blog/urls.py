from django.urls import path

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/form/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_confirm_delete')
]
