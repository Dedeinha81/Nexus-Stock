
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Gerencia o cadastro, edição e visualização de produtos.
    Inclui busca por nome/SKU e ordenação por preço.
    """
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'sku']
    ordering_fields = ['price', 'name']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Product.objects.all()
        
        if hasattr(user, 'tenant_profile'):
            return Product.objects.filter(tenant=user.tenant_profile.tenant)
        
        return Product.objects.none()

class InventoryDashboardView(APIView):
    """
    O 'Cérebro' do sistema: Calcula valor de estoque e lucro real.
    """
    def get(self, request):
        user = request.user
        
        # Filtra os produtos da empresa do usuário
        if user.is_superuser:
            queryset = Product.objects.all()
        else:
            queryset = Product.objects.filter(tenant=user.tenant_profile.tenant)

        # 1. Valor Total do Estoque (Preço de Venda * Quantidade)
        total_value = queryset.aggregate(
            total=Sum(F('price') * F('stock_quantity'))
        )['total'] or 0

        # 2. Lucro Estimado Total ( (Venda - Custo) * Quantidade )
        # Essa é a nossa métrica de inteligência de negócio!
        total_profit = queryset.aggregate(
            profit=Sum((F('price') - F('cost_price')) * F('stock_quantity'))
        )['profit'] or 0

        # 3. Alerta de Estoque Baixo (menos de 10 unidades)
        low_stock_count = queryset.filter(stock_quantity__lt=10).count()

        # 4. Contagem total de itens
        total_items = queryset.count()

        # Transformamos tudo em float para o Python não reclamar na comparação
        val_total = float(total_value)
        lucro_total = float(total_profit)

        return Response({
            "empresa": user.tenant_profile.tenant.name if not user.is_superuser else "Relatório Global",
            "estatisticas": {
                "valor_total_estoque": round(val_total, 2),
                "lucro_estimado_total": round(lucro_total, 2),
                "itens_com_estoque_baixo": low_stock_count,
                "total_de_produtos_cadastrados": total_items,
            },
            # Agora a comparação funciona sem erro:
            "mensagem_ia": "Seu lucro está saudável!" if lucro_total > (val_total * 0.2) else "Atenção: Margem de lucro abaixo de 20%."
        })