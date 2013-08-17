from django.conf.urls.defaults import *
from clothes.models import *

from django.conf.urls.defaults import url, patterns, include
from rest_framework import viewsets, routers

# ViewSets define the view behavior.


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    model = Color


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    model = Store


class ArticleTypeViewSet(viewsets.ReadOnlyModelViewSet):
    model = ArticleType


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    model = Article
    paginate_by = 10


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'colors', ColorViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'articletypes', ArticleTypeViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = patterns(
    'clothes2.views',
    url(r'^', include(router.urls)),
)
