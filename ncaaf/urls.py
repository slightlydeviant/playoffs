from django.conf.urls import patterns, include, url
from ncaaf.views import *

urlpatterns = patterns('',
    url(r'^$', ncaafHome.as_view(), name = 'ncaafhome'),
    url(r'^(?P<leagueId>\d+)/$', leaguehome, name='leaguehome'),
)
