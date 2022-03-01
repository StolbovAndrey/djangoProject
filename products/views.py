from django.shortcuts import render
from django.conf import settings
from products.models import ProductCategory, Products
import json


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
