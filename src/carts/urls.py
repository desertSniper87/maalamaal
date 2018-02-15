from django.conf.urls import url
from django.contrib import admin

from .views import ( 
                     cart_home,
                    )

urlpatterns = [
    url(r'^$', cart_home, name='cart'),
]
