from clothes.models import *

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
      'dates': Date.objects.all().order_by('-date')[:10],
      'aoutfits': AccessorizedOutfit.objects.all().order_by('-id')[:10],
      'articles': Article.objects.all().order_by('name')[:10],
      'counts': counts,
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
  return render_to_response('clothes/calendar.html', {'year': year, 'month': month})

def calendar__month(request, year, month):
  json = {}
  dates = Date.objects.filter(date__year=int(year)).filter(date__month=int(month))
  for date in dates:
    values = {'aoutfit_id': [aoutfit.id for aoutfit in date.outfits_worn.all()]}
    photo = date.first_outfit_photo()
    if photo:
      values['img_url'] = photo.src_320
    json[str(date.date)] = values
  return HttpResponse(simplejson.dumps(json), mimetype='application/json')

def problems(request):
  articles = Article.objects.filter(
      Q(accessorized_outfits__dates_worn__date__lt=F('purchase_date')) |
      Q(outfits__accessorized_outfits__dates_worn__date__lt=F('purchase_date'))
  ).distinct()
  return HttpResponse('<br>'.join(('<a href="/clothes/article/' + str(article.id) + '">' +
      article.name + '</a>') for article in articles))

def counts():
  return {
    'dates': Date.objects.count(),
    'articles': Article.objects.count(),
    'outfits': Outfit.objects.count(),
    'accessorized outfits': AccessorizedOutfit.objects.count(),
  }


