from django.db import models


class Profile(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    orders = models.ManyToManyField('orders.Order', related_name='customers')

    def __str__(self):
        return self.name
