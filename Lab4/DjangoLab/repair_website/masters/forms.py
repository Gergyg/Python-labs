from django import forms
from .models import Master

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'specialization', 'experience', 'phone_number']
