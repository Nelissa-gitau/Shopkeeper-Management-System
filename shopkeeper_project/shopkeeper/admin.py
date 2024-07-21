from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'name', 'selling_price', 'buying_price')
    search_fields = ('product_number', 'name')
    list_filter = ('selling_price', 'buying_price')
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
