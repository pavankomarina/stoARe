from django.shortcuts import render

# Create your views here.
from product.serializers import ProductSerializer
from rest_framework import generics
from product.models import Product
from stoare.pagination import LargeResultsSetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

class ProductDetail(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        data = ProductSerializer(product).data
        return Response(data)