from django.conf.urls import patterns, include, url
from accounts.views import *
from accounts.forms import MyPasswordResetForm

urlpatterns = patterns('',
    url(r'^login/', LogIn.as_view(), name='login'),
    url(r'^register/', RegisterUser.as_view(), name='register'),
    url(r'^logout/', LogOut, name='logout'),
    url(r'^password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : 'done/',
         'template_name': 'accounts/password_reset_form.html',
         'email_template_name': 'accounts/password_reset_email.html',
         'password_reset_form': MyPasswordResetForm},
        name='password_reset'),
    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'accounts/password_reset_done.html'}),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : 'accounts:login',
         'template_name': 'accounts/password_reset_confirm.html',
         'set_password_form': MySetPasswordForm},
        name='confirm'),
    url(r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
)
