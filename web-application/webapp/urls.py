from django.conf.urls import url

from webapp.views import *

app_name = 'webapp'
urlpatterns = [
    url(r'^$', IndexListView.as_view(), name='index'),
    url(r'^payment_and_delivery/$', PaymentAndDeliveryView.as_view(), name='payment_and_delivery'),
    url(r'^reviews/$', ReviewView.as_view(), name='reviews'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
    url(r'^feedback/$', FeedbackFormView.as_view(), name='feedback'),
]
