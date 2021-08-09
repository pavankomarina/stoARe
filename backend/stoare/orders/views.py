from django.db.models import query
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from orders.serializers import OrderSerializer
from rest_framework import generics
from orders.models import Order
from stoare.pagination import LargeResultsSetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class OrderList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.order_by("id")
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id', "order_by__email"]
