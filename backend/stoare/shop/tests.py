from django.http import response
from django.test import TestCase
from rest_framework import status

# Create your tests here.
from shop.models import Shop
from rest_framework.test import APIRequestFactory

class TestShopModel(TestCase):
    factory = APIRequestFactory()
    def test_shop_model(self):
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
        self.assertEqual(Shop.objects.get().name, 'test1')
        self.assertEqual(Shop.objects.get().address, '161 Rankin avenue')
        self.assertEqual(Shop.objects.get().phone, '+226123456')
        self.assertEqual(Shop.objects.get().email, 'shop1@windsor.ca')
        self.assertEqual(Shop.objects.get().rating, 4.5)
        self.assertEqual(Shop.objects.get().owner_name, 'Test')
        self.assertEqual(Shop.objects.get().description, 'Test')
        self.assertEqual(Shop.objects.get().license, 'test')

    def test_shop_list_api(self):
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
        response = self.client.get(f"/shops/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get("count"), 1)
        shop_details = data.get("results")[0]
        self.assertEqual(shop_details.get("name"), 'test1')
        self.assertEqual(shop_details.get("address"), '161 Rankin avenue')
        self.assertEqual(shop_details.get("phone"), '+226123456')
        self.assertEqual(shop_details.get("email"), 'shop1@windsor.ca')
        self.assertEqual(shop_details.get("rating"), 4.5)
        self.assertEqual(shop_details.get("owner_name"), 'Test')
        self.assertEqual(shop_details.get("description"), 'Test')
        self.assertEqual(shop_details.get("license"), 'test')
