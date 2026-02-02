
from django.contrib import admin
from .models import Tenant, TenantProfile

admin.site.register(Tenant)
admin.site.register(TenantProfile)