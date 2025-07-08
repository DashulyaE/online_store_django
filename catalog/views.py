from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 8, "cols": 30}))


class ContactView(FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} и номер телефона {phone} получены.")
