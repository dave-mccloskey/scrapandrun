from clothes.models import *
from clothes.filters import calendar_table

from django.core.urlresolvers import reverse
from django.db.models import Q, F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

import datetime
from collections import defaultdict


def overview(request):
  return render_to_response('clothes/index.html', {
    'dates': Date.objects.all().order_by('date'),
    'outfits': Outfit.objects.all(),
    'articles': Article.objects.all().order_by('name')
  })


def search(request):
  result = ''
  token = request.GET['token']
  max_matches = request.GET['max_matches']
  
  articles = Article.objects.filter(name__icontains=token)[:max_matches]
  if articles:
    result += '["' + '", "'.join((a.name for a in articles)) + '"]'
  return HttpResponse(result)


def calendar(request, year=datetime.datetime.now().year, month=datetime.datetime.now().month):
  result = ''
  
  dates = Date.objects
  if year:
    dates = dates.filter(date__year=int(year))
    if month: 
      dates = dates.filter(date__month=int(month))
  print dates
  
  # Create a dict of dict of lists like {2012: {12: [1, 2, 3]}}
  date_map = defaultdict(lambda: defaultdict(list))
  for date in dates:
    date_map[date.date.year][date.date.month].append(date.date)
  
  return render_to_response('clothes/calendar.html', {
      'dates': date_map,
  })


def calendar__month(request, year, month):
  json = {}
  dates = Date.objects.filter(date__year=int(year)).filter(date__month=int(month))
  for date in dates:
    json[str(date.date)] = {'aoutfit_id': [aoutfit.id for aoutfit in date.outfits_worn.all()] }
  return HttpResponse(simplejson.dumps(json), mimetype='application/json')
  

def problems(request):
  articles = Article.objects.filter(
      Q(accessorized_outfits__dates_worn__date__lt=F('purchase_date')) |
      Q(outfits__accessorized_outfits__dates_worn__date__lt=F('purchase_date'))
  ).distinct()
  return HttpResponse('<br>'.join(('<a href="/clothes/article/' + str(article.id) + '">' + article.name + '</a>') for article in articles))
  
#def basic_color(request, basic_color_id):
#  
#
#
#def vote(request, poll_id):
#  p = get_object_or_404(Poll, pk=poll_id)
#  try:
#  selected_choice = p.choice_set.get(pk=request.POST['choice'])
#  except (KeyError, Choice.DoesNotExist):
#  # Redisplay the poll voting form.
#  return render_to_response('polls/detail.html', {
#  'poll': p,
#  'error_message': "You didn't select a choice.",
#  }, context_instance=RequestContext(request))
#  else:
#  selected_choice.votes += 1
#  selected_choice.save()
#  # Always return an HttpResponseRedirect after successfully dealing
#  # with POST data. This prevents data from being posted twice if a
#  # user hits the Back button.
#  return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

