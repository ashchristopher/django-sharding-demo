from django.conf.urls.defaults import *

from profiles.views import BusinessView, MainView, AjaxMainView, InfoAjaxView


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^ajax/$', AjaxMainView.as_view(), name='main-ajax'),
    url(r'^ajax/shard/(?P<shard_id>\w+)/$', InfoAjaxView.as_view(), name='info'),
    url(r'^(?P<business_id>\d+)/$', BusinessView.as_view(), name='business'),
)
