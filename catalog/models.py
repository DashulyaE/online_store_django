from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}, {self.description}"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание")
    picture = models.ImageField(upload_to="catalog/foto", blank=True, null=True, verbose_name="Фото продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="products")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}, {self.description}"
