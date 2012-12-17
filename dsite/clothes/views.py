from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from clothes.models import *
from django.db.models import Q


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

