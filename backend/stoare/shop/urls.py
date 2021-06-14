
from shop.views import *
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path("", ShopList.as_view()),
    ]