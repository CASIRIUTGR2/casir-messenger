from django.conf.urls import patterns, url

urlpatterns = patterns('promotion.view',
                       url(r'^index/$', 'index'),
)