from django.contrib import messages
from django.shortcuts import HttpResponseRedirect

from products.models import Products
from baskets.models import Basket


def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets:
        Basket.objects.create(user=request.user, product=product, quantity=1)
        messages.success(request, f'Товар {product.name} добавлен в корзину')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        if basket.quantity >= product.quantity:
            messages.warning(request, 'на складе отсутствует данное количество товара')
        else:
            basket.quantity += 1
            basket.save()
            messages.success(request, f'Товар {product.name} добавлен в корзину')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basketname = basket.product.name
    basket.delete()
    messages.success(request, f'Товар {basketname} удален из корзины')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_clean(request):
    basket = Basket.objects.filter(user=request.user)
    basket.delete()
    messages.success(request, 'Корзина очищена')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
