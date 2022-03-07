from django.shortcuts import render

from products.models import ProductCategory, Products


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):

    categories = ProductCategory.objects.all()
    all_products = Products.objects.all()
    baskets = None
    context = {
        'title': 'Каталог товаров',
        'products': all_products,
        'categories': categories,
        'baskets': baskets
    }

    return render(request, 'products/products.html', context)
