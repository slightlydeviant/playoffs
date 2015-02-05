from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bowlgames.views.home', name = 'home'),
    url(r'^nfl/', include('nfl.urls', namespace = 'nfl')),
    url(r'^ncaaf/', include('ncaaf.urls', namespace = 'ncaaf')),
    url(r'^nba/', include('nba.urls', namespace = 'nba')),
    url(r'^ncaam/', include('ncaam.urls', namespace = 'ncaam')),
    url(r'^ncaaw/', include('ncaaw.urls', namespace = 'ncaaw')),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/', include('picks.urls', namespace = "picks")),
)

urlpatterns += staticfiles_urlpatterns()
