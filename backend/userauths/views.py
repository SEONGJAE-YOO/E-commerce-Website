# Restframework
import random
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

from userauths.serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
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
    

def generate_numeric_otp(length=7):
        # Generate a random 7-digit OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return otp

class PasswordEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)
        
        if user:
            user.otp = generate_numeric_otp()
            user.save()
            
            uidb64 = user.pk
            otp = user.otp
            
            link = f"http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}"
            
            # send email
                       

        return user
    
    
