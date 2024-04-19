# Restframework
from rest_framework_simplejwt.views import TokenObtainPairView
# Serializers
from userauths.serializer import (
    MyTokenObtainPairSerializer, 
    RegisterSerializer,
)
from rest_framework import generics
# Models
from userauths.models import User
from rest_framework.permissions import AllowAny

# This code defines a DRF View class called MyTokenObtainPairView, which inherits from TokenObtainPairView.
class MyTokenObtainPairView(TokenObtainPairView):
    # Here, it specifies the serializer class to be used with this view.
    serializer_class = MyTokenObtainPairSerializer

# This code defines another DRF View class called RegisterView, which inherits from generics.CreateAPIView.
class RegisterView(generics.CreateAPIView):
    # It sets the queryset for this view to retrieve all User objects.
    queryset = User.objects.all()
    # It specifies that the view allows any user (no authentication required).
    permission_classes = (AllowAny,)
    # It sets the serializer class to be used with this view.
    serializer_class = RegisterSerializer