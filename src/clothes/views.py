from clothes.models import *

from django.core.urlresolvers import reverse
from django.db.models import Q, F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from bisect import bisect
import datetime
from collections import defaultdict
from picasa import PicasaStorage

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
  props = OutfitWearingProperties.objects.filter(date__in=dates).select_related(depth=1)
  props_by_date = defaultdict(list)
  for prop in props:
    props_by_date[prop.date].append(prop)
  #return HttpResponse(props_by_date[dates[0]], mimetype='text')
  for date in props_by_date.keys():
    props = props_by_date[date]
    values = {'aoutfit_id': [prop.accessorizedoutfit.id for prop in props]}
    try:
      photo = (prop.photo for prop in props if prop.photo).next()
      values['img'] = photo.name
    except StopIteration: # No photos available
      pass
    json[str(date.date)] = values
  return HttpResponse(simplejson.dumps(json), mimetype='application/json')

def photo__src(request, size, photo_key):
  def src(photo_key, size=None):
    SIZES = (32, 48, 64, 72, 94, 104, 110, 128, 144, 150, 160, 200, 220, 288, 320, 400, 512, 576, 640, 720, 800, 912, 1024, 1152, 1280, 1440, 1600)
    img_url = PicasaStorage().url(photo_key)
    if size is not None:
      try:
        size = SIZES[bisect(SIZES, size-1)]
      except IndexError:
        size = SIZES[-1]
      url, img = img_url.rsplit ('/',1)
      return '%s/s%d/%s' %(url, size, img)
    return  img_url

  return HttpResponse(simplejson.dumps({'src': src(photo_key, int(size))}))

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


