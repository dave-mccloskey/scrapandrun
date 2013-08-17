from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from clothes.models import *

urlpatterns = patterns('clothes.views',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
