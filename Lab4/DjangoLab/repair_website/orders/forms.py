from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'service', 'quantity', 'total_price']  # Поля, которые будут отображаться в форме
