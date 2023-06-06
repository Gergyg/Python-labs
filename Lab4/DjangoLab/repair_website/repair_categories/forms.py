from django import forms
from .models import RepairCategory

class RepairCategoryForm(forms.ModelForm):
    class Meta:
        model = RepairCategory
        fields = ['name', 'description']
