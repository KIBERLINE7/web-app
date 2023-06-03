from .models import Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['mail', 'number_phone']

        widgets = {

            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
            }),

            "number_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
            }),

        }