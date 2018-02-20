#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 20.02.2018
# Last Modified Date: 20.02.2018
from django.shortcuts import render

from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request): # why there is no self arg?
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)

    if qs.count()==1:
        print("Cart ID exists")
        print(cart_id)
        cart_obj = qs.first()
        if request.user.is_authenticated == True and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()

    else:
        print('create new cart')
        cart_obj = Cart.objects.new_cart(user=request.user)
        # cart_obj = cart_create()
        request.session['cart_id']=cart_obj.id
        print("Cart_ID: ", request.session.get("cart_id"))

    return render(request, "carts/home.html", {})
