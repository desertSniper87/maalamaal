#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 12.02.2018
# Last Modified Date: 12.02.2018
from django.db import models

# from products.models import Product
from carts.models import Cart
# User = settings.AUTH_USER.MODEL

class Order(models.Model):
    order_id         = models.CharField(max_length = 120)
    cart             = models.ForeignKey(Cart, on_delete='Cascade')
    status           = models.CharField(max_length=120, default='created')
