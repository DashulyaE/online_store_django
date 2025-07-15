from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "picture", "category", "price", "publication_attribute"]

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data.get("name", "").lower()
        description = self.cleaned_data.get("description", "").lower()
        for word in forbidden_words:
            if word in name:
                self.add_error("name", f'Поле "Наименование" не может содержать слово {word}')
            if word in description:
                self.add_error("description", f'Поле "Описание" не может содержать слово {word}')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["picture"].widget.attrs.update({"class": "form-control", "type": "image"})

        self.fields["category"].widget.attrs.update({"class": "form-control"})

        self.fields["price"].widget.attrs.update({"class": "form-control", "type": "integer"})
