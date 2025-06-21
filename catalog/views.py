from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Контроллер для отображения домашней страницы"""

    return render(request, "catalog/home.html")


def contacts(request):
    """Контроллер для отображения страницы с контактной информацией и обработку данных формы"""

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} и номер телефона {phone} получены.")

    return render(request, "catalog/contacts.html")