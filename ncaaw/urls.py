from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ncaaw.views.ncaawhome', name = 'ncaawhome'),
)
