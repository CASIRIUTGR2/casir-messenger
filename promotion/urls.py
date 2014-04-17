from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('promotion.view',
                       url(r'^index/$', 'index'),
                       url(r'^dashboard/$', 'dashboard'),
                       url(r'^accounts/login/$',  login),
                       url(r'^accounts/logout/$', logout)
)