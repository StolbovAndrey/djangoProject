from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from products.models import Products, ProductCategory
from baskets.models import Basket


# @login_required
# def basket_add(request, product_id):
#     product = Products.objects.get(id=product_id)
#     baskets = Basket.objects.filter(user=request.user, product=product)
#     if not baskets:
#         Basket.objects.create(user=request.user, product=product, quantity=1)
#         messages.success(request, f'Товар {product.name} добавлен в корзину')
#         return HttpResponseRedirect(request.META['HTTP_REFERER'])
#     else:
#         basket = baskets.first()
#         if basket.quantity >= product.quantity:
#             messages.warning(request, 'на складе отсутствует данное количество товара')
#         else:
#             basket.quantity += 1
#             basket.save()
#             messages.success(request, f'Товар {product.name} добавлен в корзину')
#         return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basketname = basket.product.name
    basket.delete()
    messages.success(request, f'Товар {basketname} удален из корзины')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_clean(request):
    basket = Basket.objects.filter(user=request.user)
    basket.delete()
    messages.success(request, 'Корзина очищена')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_add(request, id):
    categories = ProductCategory.objects.all()
    all_products = Products.objects.all()
    if request.is_ajax():
        product = Products.objects.get(id=id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets:
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            if basket.quantity >= product.quantity:
                messages.warning(request, 'на складе отсутствует данное количество товара')
            else:
                basket.quantity += 1
                basket.save()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'title': 'Каталог товаров',
            'products': all_products,
            'categories': categories,
            'baskets': baskets
        }
        result = render_to_string('products/products.html', context, request.user)
        return JsonResponse({'result': result})

