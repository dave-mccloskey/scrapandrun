from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from clothes.models import Date

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Date.objects.all(),
            context_object_name='dates',
            template_name='clothes/index.html')),
#    url(r'^(?P<pk>\d+)/$',
#        DetailView.as_view(
#            model=Poll,
#            template_name='polls/detail.html')),
#    url(r'^(?P<pk>\d+)/results/$',
#        DetailView.as_view(
#            model=Poll,
#            template_name='polls/results.html'),
#        name='poll_results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
