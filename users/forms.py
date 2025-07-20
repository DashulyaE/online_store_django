from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone