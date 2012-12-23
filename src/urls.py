from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^clothes/', include('clothes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
)
