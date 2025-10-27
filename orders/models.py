from django.db import models

# Create your models here.
from django.db import models
from .order_status import OrderStatus  # adjust import if OrderStatus is defined elsewhere

class Order(models.Model):
    # existing fields (e.g., customer, total_price, etc.)
    # ...

    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name