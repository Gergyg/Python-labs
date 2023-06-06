from django.db import models
from django.utils import timezone

from customers.models import Customer
from service_types.models import ServiceType
from masters.models import Master
from parts.models import Part

class Repair(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    parts_new = models.ManyToManyField(Part)
    labour_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость работы')

    @property
    def get_total_cost(self):
        parts_cost = sum(part.price for part in self.parts_new.all())
        return self.labour_cost + parts_cost
    
    def __str__(self):
        return f"Repair {self.pk}"
