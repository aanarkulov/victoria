from django.conf.urls import url

from catalog.views import *

app_name = 'catalog'
urlpatterns = [
    url(r'^$', CatalogListView.as_view(), name='catalog'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product'),
    url(r'^product/order$', OrderFormView.as_view(), name='order_of_product'),
]