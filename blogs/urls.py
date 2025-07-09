from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetailView

app_name = BlogsConfig.name

urlpatterns = [
        path("", BlogListView.as_view(), name="blog_list"),
        path("blogs/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    ]
