from django import forms
from .models import MasterSpecialization

class MasterSpecializationForm(forms.ModelForm):
    class Meta:
        model = MasterSpecialization
        fields = ['name', 'description']
