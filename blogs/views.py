from winreg import DeleteValue

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogs.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blogs:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")