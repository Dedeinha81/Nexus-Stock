

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Essa linha diz: "Não mostre o ID, mostre o que está no __str__ do Tenant"
    tenant = serializers.StringRelatedField(read_only=True)
    
    # Fazemos o mesmo para a categoria
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'sku', 
            'price', 
            'stock_quantity', 
            'category', 
            'tenant'
        ]