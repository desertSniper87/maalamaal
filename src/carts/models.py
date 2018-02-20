#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 12.02.2018
# Last Modified Date: 20.02.2018
from django.db import models

from products.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_cart(self, user=None):
        print("User", user)
        user_obj = None
        if user is not None:
            if user.is_authenticated is True:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    """Docstring for Cart. """
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
    
