from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ncaam.views.ncaamhome', name = 'ncaamhome'),
)
