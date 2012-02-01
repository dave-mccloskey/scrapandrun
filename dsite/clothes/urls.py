from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from clothes.models import *

urlpatterns = patterns('clothes.views',
    url(r'^$', 'overview'),
    url(r'^date/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Date,
            template_name='clothes/date.html')),
    url(r'^outfit/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Outfit,
            template_name='clothes/outfit.html')),
    url(r'^article/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Article,
            template_name='clothes/article.html')),
    url(r'^article_type/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=ArticleType,
            template_name='clothes/article_type.html')),
    url(r'^color/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Color,
            template_name='clothes/color.html')),
    #url(r'^basic_color/(?P<pk>\w+)/$', 'basic_color'),
)
