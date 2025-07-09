from django.views.generic import ListView


# Create your views here.
class BlogListView(ListView):
    model = Blogs
