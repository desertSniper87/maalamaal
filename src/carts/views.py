#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 20.02.2018
# Last Modified Date: 21.02.2018
from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.get(user=None)
    return cart_obj

def cart_home(request): # why there is no self arg?
    cart_obj, new_obj= Cart.objects.new_or_get(request)

    products = cart_obj.products.all() 
    total = 0

    for x in products:
        total += x.price

    print('total: ', total)
    cart_obj.total = total
    cart_obj.save()

    return render(request, "carts/home.html", {})

def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(product_obj)
    # cart_obj.title
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)


    # return redirect(product_obj.get_absolute_url())
    return redirect("carts:home")
