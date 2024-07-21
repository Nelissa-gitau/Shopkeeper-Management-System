from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_number', 'name', 'selling_price', 'buying_price']
    
    def clean_selling_price(self):
        selling_price = self.cleaned_data['selling_price']
        if selling_price <= 0:
            raise forms.ValidationError('Selling price must be greater than zero.')
        return selling_price
    
    def clean_buying_price(self):
        buying_price = self.cleaned_data['buying_price']
        if buying_price <= 0:
            raise forms.ValidationError('Buying price must be greater than zero.')
        return buying_price
