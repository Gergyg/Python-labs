from django.contrib import admin
from .models import MasterSpecialization

# Register your models here.
@admin.register(MasterSpecialization)
class MasterSpecializationAdmin(admin.ModelAdmin):
    pass
