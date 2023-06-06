from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'  # Или укажите конкретные поля, которые нужно отображать в форме
