
from utils.views import *
from django.urls import path

app_name = 'utils'

urlpatterns = [
    path("message/", SendMessage.as_view())
    ]