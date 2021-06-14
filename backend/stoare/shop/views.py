from django.shortcuts import render

# Create your views here.
from shop.serializers import ShopSerializer
from rest_framework import generics
from shop.models import Shop
from stoare.pagination import LargeResultsSetPagination

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.filter(is_active=True)
    serializer_class = ShopSerializer
    pagination_class = LargeResultsSetPagination

