from django.contrib import admin
from .models import Master

# Register your models here.
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    pass
