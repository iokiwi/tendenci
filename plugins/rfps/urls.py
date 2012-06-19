from django.conf.urls.defaults import patterns, url
from rfps.feeds import LatestEntriesFeed

urlpatterns = patterns('rfps.views',                  
    url(r'^rfps/$', 'search', name="rfps"),
    url(r'^rfps/search/$', 'search_redirect', name="rfps.search"),
    url(r'^rfps/feed/$', LatestEntriesFeed(), name='rfps.feed'),
    url(r'^rfps/(?P<slug>[\w\-\/]+)/$', 'detail', name="rfps.detail"),
)
