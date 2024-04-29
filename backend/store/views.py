from django.shortcuts import render
from store.models import Category, Product
from store.serializer import CategorySerializer, ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        slug = self.kwargs['slug']
        return Product.objects.get(slug=slug)