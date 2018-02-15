#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 12.02.2018
# Last Modified Date: 12.02.2018
from django.db import models

from products.models import Product
User = settings.AUTH_USER.MODEL

class Cart(models.Model):
    """Docstring for Cart. """
    user      =             models.ForeignKey(User, null=True, blank=True)
    products  =             models.ManyToOneField()  
    total     =             models.DecimalField() 
    updatd    =             models.DateTimeField(auto_now=True)
    timestamp =             models.DateTimeField(auto_now_add=True)
    
