from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.apps import apps
from .views import hello_world, home_page, about_page, contact_page, login_page, register_page
products_name = apps.get_app_config('products').verbose_name

urlpatterns = [
    url(r'^hello/$', hello_world),

    url(r'^$', home_page),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', about_page),
    url(r'^contact/$', contact_page),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),

    url(r'^products/', include(('products.urls', products_name), namespace='products')),
]
# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# if settings.DEBUG:
    # urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
