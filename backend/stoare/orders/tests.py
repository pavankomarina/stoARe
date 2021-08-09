from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from rest_framework import status
from orders.models import Order
from product.models import Product
from shop.models import Shop
from rest_framework.test import APIRequestFactory
from django.urls import include, path, reverse

class TestShopModel(TestCase):
    factory = APIRequestFactory()
    def test_order_model(self):
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
        user = User.objects.create(
            first_name="test",
            email="test@test.com",
            username="testuser"
        )
        product = Product.objects.create(
            name="product_test",
            description="product description",
            price=123.5,
            shop=shop,
            rating=3.5
        )
        order = Order.objects.create(
            order_by=user,
            product=product,
            quantity=5
        )
        self.assertEqual(Order.objects.get().quantity, 5)
        self.assertEqual(Order.objects.get().product.name, "product_test")
        self.assertEqual(Order.objects.get().order_by.email, "test@test.com")