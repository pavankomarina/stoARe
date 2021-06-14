
from product.views import *
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('<int:product_id>/', ProductDetail.as_view()),
    path("", ProductList.as_view()),
    ]