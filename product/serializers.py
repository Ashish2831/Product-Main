from rest_framework import serializers
from .models import ProductMainModel, ProductColourModel, ProductImageModel

# Create your serializers here.

class ProductMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainModel
        fields = "__all__"
        
        
class ProductColourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColourModel
        fields = "__all__"
        
        
class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__"
        