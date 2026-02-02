
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, InventoryDashboardView 

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    # Colocamos o dashboard PRIMEIRO
    path('dashboard/', InventoryDashboardView.as_view(), name='inventory-dashboard'),
    
    # Depois as rotas automáticas dos produtos
    path('', include(router.urls)),
]