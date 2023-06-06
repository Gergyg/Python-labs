from django.contrib import admin
from .models import RepairCategory

# Register your models here.
@admin.register(RepairCategory)
class RepairCategoryAdmin(admin.ModelAdmin):
    pass