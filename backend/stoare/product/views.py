from django.db.models import query
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from product.serializers import ProductSerializer, ProductDetailSerializer
from rest_framework import generics
from product.models import Product
from stoare.pagination import LargeResultsSetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(available=True).order_by("id")
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop_id']

class ProductDetail(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializer
    pagination_class = LargeResultsSetPagination

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        data = ProductDetailSerializer(product, context={"request":self.request}).data
        return Response(data)
