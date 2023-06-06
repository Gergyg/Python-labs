from django.contrib import admin
from .models import RepairObject

# Register your models here.
@admin.register(RepairObject)
class RepairObjectAdmin(admin.ModelAdmin):
    pass