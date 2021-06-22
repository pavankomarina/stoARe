from django.shortcuts import render

# Create your views here.
from product.serializers import ProductSerializer
from rest_framework import generics
from product.models import Product
from stoare.pagination import LargeResultsSetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(available=True).order_by("id")
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

class ProductDetail(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        data = ProductSerializer(product, context={"request":self.request}).data
        return Response(data)
