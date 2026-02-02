
import uuid
from django.db import models
from django.conf import settings # Importante para referenciar o usuário do sistema

class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome da Empresa")
    subdomain = models.SlugField(unique=True, verbose_name="Subdomínio/Identificador")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Empresa Cliente"
        verbose_name_plural = "Empresas Clientes"


class TenantDataModel(models.Model):
    """
    Modelo base para garantir o isolamento de dados (Multi-tenancy).
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TenantProfile(models.Model):
    """
    Vincula um Usuário do Django a um Tenant específico.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='tenant_profile'
    )
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.tenant.name}"

    class Meta:
        verbose_name = "Perfil de Usuário por Empresa"
        verbose_name_plural = "Perfis de Usuários por Empresas"