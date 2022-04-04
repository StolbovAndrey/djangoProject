from django.shortcuts import render

from products.models import ProductCategory, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):

    categories = ProductCategory.objects.all()
    baskets = None
    context = {
        'title': 'Каталог товаров',
        'categories': categories,
        'baskets': baskets
    }
    if category_id:
        products = Products.objects.filter(category_id=category_id)
    else:
        products = Products.objects.all()

    pag = Paginator(products, 3)
    try:
        products_pag = pag.page(page)
    except PageNotAnInteger:
        products_pag = pag.page(1)
    except EmptyPage:
        products_pag = pag.page(pag.num_pages)

    context['products'] = products_pag

    return render(request, 'products/products.html', context)
