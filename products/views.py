from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Nur Store'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Nur store',
        'products': products_paginator,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1 )
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(requset, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(requset.META['HTTP_REFERER'])


def dop(requset):
    fruits = ['Яблоко', 'Банан', 'Апельсин', 'Киви']
    context = {'fruits': fruits}
    return render(requset, 'products/dop.html', context)
