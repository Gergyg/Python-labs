from django.contrib import admin
from .models import Repair

# Register your models here.
@admin.register(Repair)
class CustomUserAdmin(admin.ModelAdmin):
    pass