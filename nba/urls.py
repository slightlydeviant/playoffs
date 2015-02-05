from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'nba.views.nbahome', name = 'nbahome'),
)
