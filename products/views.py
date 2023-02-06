from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    categories = None
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'products/product_detail.html', {
        'product': product,
    })