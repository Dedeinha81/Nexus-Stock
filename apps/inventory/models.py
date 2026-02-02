
from django.db import models
from apps.tenants.models import TenantDataModel 
from simple_history.models import HistoricalRecords

class Category(TenantDataModel): 
    name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(TenantDataModel): # Mantemos a herança do TenantDataModel
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    # Preços para a "IA" calcular o lucro depois
    price = models.DecimalField(max_digits=10, decimal_places=2) # Preço de Venda
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # NOVO: Preço de Custo
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    history = HistoricalRecords()
    
    def __str__(self):
        return f"{self.name} ({self.sku})"