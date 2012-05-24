from django.conf.urls.defaults import *

from profiles.views import BusinessView, MainView, AjaxMainView


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^ajax/$', AjaxMainView.as_view(), name='main-ajax'),
    url(r'^(?P<business_id>\d+)/$', BusinessView.as_view(), name='business'),
)
