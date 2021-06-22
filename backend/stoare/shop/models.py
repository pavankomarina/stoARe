from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField
from phonenumber_field.modelfields import PhoneNumberField


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


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
    image = models.ForeignKey(Image, related_name='shops', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name