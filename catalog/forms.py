from django import forms
from .models import Product

FORBIDDEN_WORDS = [
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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "picture", "category", "price", "publication_attribute"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["picture"].widget.attrs.update({"class": "form-control", "type": "image"})

        self.fields["category"].widget.attrs.update({"class": "form-control"})

        self.fields["price"].widget.attrs.update({"class": "form-control", "type": "integer"})

    def clean_name(self):
        name = self.cleaned_data.get("name", "").lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f'Поле "Наименование" не может содержать слово {word}')
        return self.cleaned_data["name"]

    def clean_description(self):
        description = self.cleaned_data.get("description", "").lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f'Поле "Описание" не может содержать слово {word}')
        return self.cleaned_data["description"]
