from django.shortcuts import render
from django.conf import settings
from .models import ProductCategory, Products
import json


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):

    allProducts = Products.objects.all()
    context = {'title': 'Каталог товаров', 'products': allProducts}

    return render(request, 'products/products.html', context)
