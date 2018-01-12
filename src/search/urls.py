from django.conf.urls import url
from django.contrib import admin

from products.views import (
                    SearchProductView,
                    )

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='search'),
]
