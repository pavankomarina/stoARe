from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_auth.views import UserAPIView, RegisterView, MyTokenObtainPairView

urlpatterns = [
    # Your other URL entries.
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    
]