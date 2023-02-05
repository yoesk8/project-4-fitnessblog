from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'products/product_detail.html', {
        'product': product,
    })