"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Importamos as visualizações do drf-spectacular (Swagger)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota da sua API de Inventário 
    path('api/', include('apps.inventory.urls')),    # --- NOVAS ROTAS DA DOCUMENTAÇÃO ---
    
    # Gera o arquivo de esquema da API (o "mapa" do sistema)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Cria a interface visual bonita (Swagger) para testar a API
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
