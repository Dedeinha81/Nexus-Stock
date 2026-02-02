
from django.contrib import admin
from .models import Category, Product
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Product)
class ProductAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'sku', 'price', 'stock_quantity']
    search_fields = ['name', 'sku']

@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin):
    list_display = ['name']