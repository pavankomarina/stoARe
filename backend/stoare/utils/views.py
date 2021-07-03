from django.http.response import ResponseHeaders
from django.shortcuts import render
from django.conf import settings
from utils.constants import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.models import Shop
from rest_framework.generics import GenericAPIView
from utils.serializers import MessageSerializer

class SendMessage(GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request, format=None):
        """
        sends message and email to shop
        """

        from twilio.rest import Client
        from django.core.mail import send_mail
        try:
            data = request.data
            message_type = data.get("message_type")
            shop_id = data.get("shop_id")
            if not message_type:
                return Response({"details": "Message ID required"}, status=status.HTTP_400_BAD_REQUEST)
            if not shop_id:
                return Response({"details": "Shop ID required"}, status=status.HTTP_400_BAD_REQUEST)
            shop : Shop = Shop.objects.get(pk=shop_id, is_active=True)

            # send sms
            if message_type == "sms":
                account_sid = settings.TWILIO_ACCOUNT_SID
                auth_token = settings.TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                    messaging_service_sid=settings.TWILIO_MESSAGING_SERVICE_SID, 
                    body=SMS_BODY,
                    to=str(shop.phone))
                return Response(status=status.HTTP_200_OK)

            # send email
            elif message_type == "email":
                send_mail(
                    EMAIL_SUBJECT,
                    EMAIL_MESSAGE,
                    settings.EMAIL_HOST_USER,
                    [shop.email],
                    fail_silently=False,
                )
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)