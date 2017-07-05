from django.conf.urls import url
from shop.views import product_detail,product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
