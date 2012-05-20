from django.conf.urls.defaults import *

from profiles.views import BusinessView


urlpatterns = patterns('',
    url(r'^(?P<business_id>\d+)/$', BusinessView.as_view(), name='business'),
)
