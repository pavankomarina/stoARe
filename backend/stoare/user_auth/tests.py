from django.http import response
from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from django.urls import include, path, reverse

class TestShopModel(TestCase):
    factory = APIRequestFactory()
    def test_user_model(self):
        data = dict(
            username="test",
            password="test@123",
            email="test@test.com",
            first_name="Test",
            last_name="Lastname"
        )
        response = self.client.post(
            "/auth/register/", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)