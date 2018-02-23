#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 23.02.2018
# Last Modified Date: 23.02.2018
from django.db import models

from carts.models import Cart

ORDER_STATUS_CHOICES = (
                        ('created', 'Created'),
                        ('paid', 'Paid'),
                        ('shipped', 'Shipped'),
                        ('refunded', 'Refunded'), 
                       )

class Order(models.Model):
    order_id         = models.CharField(max_length = 120)
    cart             = models.ForeignKey(Cart, on_delete='Cascade')
    status           = models.CharField(max_length=120, default='created')
    order_total      = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id
