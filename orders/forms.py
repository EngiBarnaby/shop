from django import forms
from .models import Order


delivery_choice = [
                    ("Доставка курьером", "Доставка курьером"),
                    ("Самовывоз", "Самовывоз"),
                    ]

verification_choice = [
        ("Смс", "Смс"),
        ("Звонок оператора", "Звонок оператора"),
]

class OrderForm(forms.ModelForm):
    # delivery = models.ChoiceField(widget = forms.RadioSelect, choices=delivery_choice)
    # verification = models.ChoiceField(widget = forms.RadioSelect, choices=verification_choice)
    class Meta:
        model = Order
        exclude = ['create', 'update', 'paid']

        labels = {
            'first_name' : "Имя",
            'last_name' : "Фамилия",
            'phone_number' : "Номер телефона",
            'address' : 'Адрес',
        }

        widgets = {'delivery' :forms.RadioSelect(attrs={'name': 'rating'}, choices=delivery_choice),
                    'verification' : forms.RadioSelect(attrs={'name': 'rating'}, choices=verification_choice)}
