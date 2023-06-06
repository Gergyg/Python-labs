from django.db import models
from repair_categories.models import RepairCategory

class RepairObject(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(RepairCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
