from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog
    paginate_by = 3

    extra_context = {
        'title': 'Личный блок - MyBlog',
        'section_name': 'Каталог статей',
    }


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'preview', 'content', 'is_published',)
    success_url = reverse_lazy('blog:article_list')

