#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 23.02.2018
# Last Modified Date: 23.02.2018
from django.db import models
from django.db.models.signals import pre_save

from carts.models import Cart
from maalamaal.utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
                        ('created', 'Created'),
                        ('paid', 'Paid'),
                        ('shipped', 'Shipped'),
                        ('refunded', 'Refunded'), 
                       )

class Order(models.Model):
    order_id         = models.CharField(max_length = 120, blank=True)
    cart             = models.ForeignKey(Cart, on_delete='Cascade')
    status           = models.CharField(max_length=120, default='created')
    order_total      = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Order)
    
