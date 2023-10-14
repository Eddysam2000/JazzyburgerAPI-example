from rest_framework import viewsets, permissions
from .models import Product
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ProductSerializer, ProductDetailSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        else:
            return self.serializer_class