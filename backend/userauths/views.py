# Restframework
from rest_framework_simplejwt.views import TokenObtainPairView
# Serializers
from userauths.serializer import MyTokenObtainPairSerializer


# This code defines a DRF View class called MyTokenObtainPairView, which inherits from TokenObtainPairView.
class MyTokenObtainPairView(TokenObtainPairView):
    # Here, it specifies the serializer class to be used with this view.
    serializer_class = MyTokenObtainPairSerializer
