from django import forms
from .models import RepairObject

class RepairObjectForm(forms.ModelForm):
    class Meta:
        model = RepairObject
        fields = '__all__'
