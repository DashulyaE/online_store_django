from winreg import DeleteValue

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogs.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
