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
    url(r'^aoutfit/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=AccessorizedOutfit,
            context_object_name='aoutfit',
            template_name='clothes/aoutfit.html')),
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
    url(r'^search/', 'search'),
    url(r'^calendar/', 'calendar'),
    url(r'^calendar/(\d{4})/(\d{1,2})/', 'calendar'),
    url(r'^problems/$', 'problems'),
    # JSON URLs
    url(r'json/calendar/month/(\d{4})/(\d{1,2})/$', 'calendar__month'),
)

