from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:product_list')
