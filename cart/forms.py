from django import forms
from shop.models import ValueAndPrices, Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
values = [(i, str(i)) for i in range(1, 5)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class ValueForm(forms.Form):
    def __init__(self, product_id, *args, **kwargs):
        super(ValueForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ChoiceField(
            choices=[(i['value'], str(i['value'])) for i in Product.objects.get(id=product_id).prices.values('value')]
        )
