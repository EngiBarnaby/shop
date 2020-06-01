from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField

delivery_choice = [
                    ("Доставка курьером", "Доставка курьером"),
                    ("Самовывоз", "Самовывоз"),
                    ]

verification_choice = [
        ("Смс", "Смс"),
        ("Звонок оператора", "Звонок оператора"),
]

adress_choice = [ (str(item.adress), str(item.adress)) for item in ShopAdress.objects.all() ]



class OrderForm(forms.ModelForm):
    # adress_all = forms.ChoiceField(choices=adress_choice, widget=forms.RadioSelect)
    # adress = models.ChoiceField(widget = forms.RadioSelect, choices=adress_choice)
    # verification = models.ChoiceField(widget = forms.RadioSelect, choices=verification_choice)

    class Meta:
        model = Order
        exclude = ['create', 'update', 'paid', 'delivery']

        labels = {
            'delivery' : 'Адресс доставки',
            'first_name' : "Имя",
            'last_name' : "Фамилия",
            'phone_number' : "Номер телефона",
            'address' : 'Адрес',
        }

        widgets = {'verification' : forms.RadioSelect(attrs={'class':'custom-control-input custom-control-label'}, choices=verification_choice),
                        'adress_choice' : forms.RadioSelect(attrs={'class':'custom-control-input custom-control-label'}, choices=adress_choice)}


        # widgets = {'verification' : forms.RadioSelect(attrs={'class':'custom-control-input custom-control-label'}, choices=verification_choice)}

        # widgets = {'delivery' :forms.RadioSelect(attrs={'class':'custom-control-input custom-control-label'}, choices=delivery_choice),
        #             'verification' : forms.RadioSelect(attrs={'class':'custom-control-input custom-control-label'}, choices=verification_choice)}
