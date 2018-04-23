from django.conf.urls import url

from news.views import *

app_name = 'news'
urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view(), name='one_news'),
    url(r'^success/subscribe/$', SubscriberFormView.as_view(), name='subscriber'),
]
