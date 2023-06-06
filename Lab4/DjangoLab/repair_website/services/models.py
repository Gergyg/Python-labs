from django.db import models
from service_types.models import ServiceType

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
