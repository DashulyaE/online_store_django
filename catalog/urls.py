from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='home'),
    path('catalog/<int:pk>', product_detail, name='product_detail'),
    path("contacts/", contacts, name="contacts"),
]