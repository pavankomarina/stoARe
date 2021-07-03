from rest_framework import serializers
from django.conf import settings

from product.models import Product
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    shop_id = serializers.SerializerMethodField()
    shop_name = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'rating', 'image', 'shop_id', 'shop_name']

    def get_image(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return ""
        return f"{request.scheme}://{request.META.get('HTTP_HOST')}{settings.MEDIA_URL}{obj.image.image}"

    def get_shop_id(self, obj):
        return obj.shop and obj.shop.pk
    
    def get_shop_name(self, obj):
        return obj.shop and obj.shop.name