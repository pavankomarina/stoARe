from rest_framework import serializers
from django.conf import settings

from product.models import Product
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'rating', 'image']

    def get_image(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return ""
        return f"{request.scheme}://{request.META.get('HTTP_HOST')}{settings.MEDIA_URL}{obj.image.image}"
