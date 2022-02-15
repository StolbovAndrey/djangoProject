from django.shortcuts import render
import json


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):

    with open('E:/projects/geekshop-server/geekshop/static/vendor/img/products/fixtures/data.json', encoding='utf-8') as file:
        context = json.load(file)

    return render(request, 'products/products.html', context)
