from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin
from blog.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "publication_attribute")
    search_fields = (
        "title",
    )