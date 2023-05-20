from django.urls import reverse_lazy, reverse
from django.views import generic
from django.utils.text import slugify
from transliterate import translit
from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {
        "title": "Новости дня"
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def get_object(self, queryset=None):
        object_item = super().get_object(queryset)
        object_item.increase_count_of_view()
        object_item.save()
        return object_item


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'content', 'image', 'create_date')
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        post = form.save(commit=False)
        eng_title = translit(post.title, 'ru', reversed=True)
        post.slug = slugify(eng_title, allow_unicode=True)
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'create_date')

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset
