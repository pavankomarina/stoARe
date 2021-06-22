from django.db import models
from shop.models import Shop, Image

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    shop = models.ForeignKey(Shop, related_name="products", on_delete=models.CASCADE)
    rating = models.FloatField()
    available = models.BooleanField(default=True)
    image = models.ForeignKey(Image, related_name='product_images', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name