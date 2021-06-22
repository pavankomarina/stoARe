from rest_framework import serializers
from django.conf import settings

from shop.models import Shop
class ShopSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ["name", "address", "phone", "email", "rating", "owner_name", "description", "license", "image"]

    def get_image(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return ""
        return f"{request.scheme}:{request.META.get('HTTP_HOST')}{settings.MEDIA_URL}{obj.image.image}"