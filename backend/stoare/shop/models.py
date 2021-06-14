from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Shop(models.Model):
    name=models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField()
    email = models.CharField(max_length=25)
    rating = models.FloatField()
    owner_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    license = models.TextField()

    def __str__(self):
        return self.name