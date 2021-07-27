from django.db import models
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

class ProductDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    shop_id = serializers.SerializerMethodField()
    shop_name = serializers.SerializerMethodField()
    related_image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'rating', 'image', 'shop_id', 'shop_name', 'related_image_urls']

    def get_image(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return ""
        return f"{request.scheme}://{request.META.get('HTTP_HOST')}{settings.MEDIA_URL}{obj.image.image}"

    def get_shop_id(self, obj):
        return obj.shop and obj.shop.pk
    
    def get_shop_name(self, obj):
        return obj.shop and obj.shop.name
    
    def get_related_image_urls(self, obj):
        result = list()
        request = self.context.get("request")
        for image in obj.related_images.all():
            result.append(f"{request.scheme}://{request.META.get('HTTP_HOST')}{settings.MEDIA_URL}{image.image}")
        return result
