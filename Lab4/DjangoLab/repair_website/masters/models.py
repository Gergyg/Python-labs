from django.db import models
from master_specializations.models import MasterSpecialization

class Master(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(MasterSpecialization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
