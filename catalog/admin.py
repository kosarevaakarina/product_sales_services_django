from django.contrib import admin

from catalog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_filter = ('name',)
    search_fields = ('name', 'phone')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'num_of_version', 'title')
    list_filter = ('product', 'title',)
    search_fields = ('product',)
