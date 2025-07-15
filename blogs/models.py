from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    preview = models.ImageField(upload_to="blogs/image", verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Дата создания")
    publication_attribute = models.BooleanField(verbose_name="Признак публикации")
    number_of_views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "created_at", "number_of_views"]

    def __str__(self):
        return self.title
