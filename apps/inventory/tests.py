
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product
from apps.tenants.models import Tenant, TenantProfile

class InventoryDashboardTest(TestCase):
    def setUp(self):
        # Criamos o cenário: Empresa, Usuário e Produto
        self.tenant = Tenant.objects.create(name="Farmácia Teste")
        self.user = User.objects.create_user(username='testuser', password='password123')
        TenantProfile.objects.create(user=self.user, tenant=self.tenant)
        
        # Produto com Custo 10 e Venda 15 (Lucro esperado: 5 por unidade)
        Product.objects.create(
            name="Produto Teste",
            sku="TEST-001",
            price=15.00,
            cost_price=10.00,
            stock_quantity=2,
            tenant=self.tenant
        )

    def test_dashboard_calculation(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/api/dashboard/')
        
        # Verificamos se o lucro calculado pela sua View é 10.00 ( (15-10) * 2 )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['estatisticas']['lucro_estimado_total'], 10.00)