from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from poolapp.apps.post.models import Tourney
 
# def index(request):
#   return render_to_response('find/index.html', context_instance=RequestContext(request))

def index(request):
  state_list = Tourney.objects.order_by().values_list('state', flat=True).distinct()
  context = {'state_list': state_list}
  return render(request, 'find/index.html', context)

def state(request, state_id):
  tourney_list = Tourney.objects.filter(state=state_id)
  context = {'tourney_list': tourney_list}
  return render(request, 'find/state.html', context)

# def state(request, state_id):
#     return HttpResponse("You're looking at state %s." % state_id)
