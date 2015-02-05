from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ncaaf.views.ncaafhome', name = 'ncaafhome'),
)
