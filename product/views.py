from rest_framework import viewsets
from .models import ProductMainModel, ProductColourModel, ProductImageModel
from .serializers import ProductMainModelSerializer, ProductColourModelSerializer, ProductImageModelSerializer

# Create your views here.

class ProductMainModelViewset(viewsets.ModelViewSet):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainModelSerializer


class ProductColourModelViewset(viewsets.ModelViewSet):
    queryset = ProductColourModel.objects.all()
    serializer_class = ProductColourModelSerializer


class ProductImageModelViewset(viewsets.ModelViewSet):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageModelSerializer
    