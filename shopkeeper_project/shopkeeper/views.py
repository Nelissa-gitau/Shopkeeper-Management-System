from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.db.models import Max, Min, Avg, Count


def homepage(request):
    return render(request, 'shopkeeper/home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shopkeeper/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()

    stats = Product.objects.aggregate(
        total_products=Count('id'),
        avg_selling_price=Avg('selling_price'),
        avg_buying_price=Avg('buying_price'),
        highest_selling_price=Max('selling_price'),
        lowest_selling_price=Min('selling_price'),
        highest_buying_price=Max('buying_price'),
        lowest_buying_price=Min('buying_price')
    )
    return render(request, 'shopkeeper/product_list.html', {
        'products': products,
        'total_products': stats['total_products'],
        'avg_selling_price': stats['avg_selling_price'] or 0,
        'avg_buying_price': stats['avg_buying_price'] or 0,
        'highest_selling_price': stats['highest_selling_price'] or 0,
        'lowest_selling_price': stats['lowest_selling_price'] or 0,
        'highest_buying_price': stats['highest_buying_price'] or 0,
        'lowest_buying_price': stats['lowest_buying_price'] or 0,
    })

def update_product(request, product_number):
    product = get_object_or_404(Product, product_number=product_number)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shopkeeper/update_product.html', {'form': form, 'product': product})

def delete_product(request, product_number):
    product = get_object_or_404(Product, product_number=product_number)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'shopkeeper/delete_product.html', {'product': product})
