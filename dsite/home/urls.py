from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from clothes.models import *

urlpatterns = patterns('clothes.views',
    url(r'^$', direct_to_template, {'template': 'index.html'}),
)
