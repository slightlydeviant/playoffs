from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'nfl.views.nflhome', name = 'nflhome'),
)
