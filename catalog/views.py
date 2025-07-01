from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def product_list(request):
    """Контроллер для отображения главной страницы со списком товаров"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def product_detail(request, pk):
    """Контроллер для отображения страницы с описанием товара"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    """Контроллер для отображения страницы с контактной информацией и обработку данных формы"""

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} и номер телефона {phone} получены.")

    return render(request, "catalog/contacts.html")