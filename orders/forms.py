from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['create', 'update', 'paid']

        labels = {
            'first_name' : "Имя",
            'last_name' : "Фамилия",
            'phone_number' : "Номер телефона",
            'address' : 'Адрес',
        }
