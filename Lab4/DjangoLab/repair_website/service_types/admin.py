from django.contrib import admin
from .models import ServiceType

# Register your models here.
@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass
