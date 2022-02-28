from django.shortcuts import HttpResponseRedirect

from products.models import Products
from baskets.models import Basket


def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets:
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_clean(request):
    basket = Basket.objects.filter(user=request.user)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
