from django.db import models
from django.utils import timezone

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

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}% off)"

    def is_valid(self):
        """Check if the coupon is currently valid."""
        today = timezone.now().date()
        return self.is_active and self.valid_from <= today <= self.valid_until