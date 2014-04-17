from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'casir_messenger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url("^$", "promotion.views.index", name="index"),
#     url("^promotion/", include('promotion.urls')),
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^index/$', 'index')
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$',logout),
    url(r'^/accounts/profile/$', 'promotion.views.dashboard')
)
