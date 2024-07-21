from django.db import models

class Product(models.Model):
    product_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} (#{self.product_number})'
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
