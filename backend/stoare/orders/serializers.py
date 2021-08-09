from django.db import models
from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
    
    def create(self, data):
        order_by = data.get("order_by")
        product = data.get("product")
        quantity = data.get("quantity")
        msg_html = render_to_string(
            'confirm_order.html', 
            {
                "quantity": quantity, 
                "product_name":product.name,
                "price": quantity*product.price,
                "first_name":order_by.first_name
            }
        )
        send_mail(
            'Your order is confirmed',
            "Hello",
            settings.EMAIL_HOST_USER,
            [order_by.email],
            html_message=msg_html,
            fail_silently=False
        )
        order_instance = Order.objects.create(**data)
        return order_instance