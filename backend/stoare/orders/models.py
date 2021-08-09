from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    ORDER_CHOICES = [
        ("CONFIRMED", "CONFIRMED"),
        ("CANCELLED", "CANCELLED")
    ]
    quantity = models.IntegerField(default=1)
    order_by = models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_CHOICES, default="CONFIRMED")

    def __str__(self):
        return f"{self.order_by.first_name} - {self.product.name} - {self.quantity}"