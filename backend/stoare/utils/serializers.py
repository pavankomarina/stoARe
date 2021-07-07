from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    shop_id = serializers.IntegerField(default=1)
    message = serializers.CharField()