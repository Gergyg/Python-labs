from django.db import models
from services.models import Service
from customers.models import Customer

class Sale(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Sale #{self.id}"
