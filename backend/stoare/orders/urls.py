
from orders.views import *
from django.urls import path

app_name = 'orders'

urlpatterns = [
        path("", OrderList.as_view()),
    ]