from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        products = get_products_from_cache()
        return products.filter(publication_attribute=True)

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy('users:login')

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Product
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy('users:login')

    def test_func(self):
        product = self.get_object()
        return self.request.user.has_perm('catalog.delete_product') or self.request.user == product.owner

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 8, "cols": 30}))


class ContactView(LoginRequiredMixin, FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} и номер телефона {phone} получены.")


def category_products_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = get_products_by_category(category_id)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'catalog/category_products.html', context)

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'catalog/base.html', {'categories': categories})