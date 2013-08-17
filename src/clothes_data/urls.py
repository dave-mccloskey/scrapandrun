from django.conf.urls.defaults import *
from clothes.models import *

from django.conf.urls.defaults import url, patterns, include
from rest_framework import viewsets, routers

# ViewSets define the view behavior.


class ColorViewSet(viewsets.ModelViewSet):
    model = Color


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'colors', ColorViewSet)

urlpatterns = patterns(
    'clothes2.views',
    url(r'^', include(router.urls)),
)
