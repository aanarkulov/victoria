from django import forms
from catalog.models import OrderOfProduct


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderOfProduct
        fields = ('name', 'phone', 'email', 'id_product', 'color', 'quantity')
