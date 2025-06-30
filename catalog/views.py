from django.shortcuts import render
from catalog.models import Product

def dog_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/base.html', context)
