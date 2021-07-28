from django.http import response
from django.test import TestCase
from rest_framework import status
from product.models import Product
from shop.models import Shop
from rest_framework.test import APIRequestFactory
from django.urls import include, path, reverse

class TestShopModel(TestCase):
    factory = APIRequestFactory()
    def test_product_model(self):
        shop = Shop.objects.create(
            name="test1",
            address="161 Rankin avenue",
            phone="+226123456",
            email="shop1@windsor.ca",
            rating="4.5",
            owner_name="Test",
            description="Test",
            license="test"
        )
        product = Product.objects.create(
            name="product_test",
            description="product description",
            price=123.5,
            shop=shop,
            rating=3.5
        )
        self.assertEqual(Product.objects.get().name, 'product_test')
        self.assertEqual(Product.objects.get().description, 'product description')
        self.assertEqual(Product.objects.get().price, 123.5)
        self.assertEqual(Product.objects.get().rating, 3.5)

    def test_product_list_api(self):
        shop = Shop.objects.create(
            name="test1",
            address="161 Rankin avenue",
            phone="+226123456",
            email="shop1@windsor.ca",
            rating="4.5",
            owner_name="Test",
            description="Test",
            license="test"
        )
        product = Product.objects.create(
            name="product_test",
            description="product description",
            price=123.5,
            shop=shop,
            rating=3.5
        )
        response = self.client.get(f"/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get("count"), 1)
        product_details = data.get("results")[0]
        self.assertEqual(product_details.get("name"), 'product_test')
        self.assertEqual(product_details.get("description"), 'product description')
        self.assertEqual(product_details.get("price"), 123.5)
        self.assertEqual(product_details.get("rating"), 3.5)