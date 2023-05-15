from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_of_view')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
