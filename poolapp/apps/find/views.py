import phonenumbers

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from poolapp.apps.post.models import Tourney
 
# def index(request):
#   return render_to_response('find/index.html', context_instance=RequestContext(request))

def index(request):
  state_list = Tourney.objects.order_by('state').values_list('state', flat=True).distinct()
  context = {'state_list': state_list}
  return render(request, 'find/index.html', context)

def state(request, state_id):
  tourney_list = Tourney.objects.filter(state=state_id)
  context = {'tourney_list': tourney_list}
  return render(request, 'find/state.html', context)

# Example of just printing some text to the page wth an HTTP response
# def state(request, state_id):
#     return HttpResponse("You're looking at state %s." % state_id)

def tourney(request, tourney_id):
  # Tournament IDs should be unique, so only select the first (and only) item
  # from the QuerySet
  tourney = Tourney.objects.filter(tourney_id=tourney_id).distinct()[0]
  tourney.formatted_contact_phone = phonenumbers.format_number(
      phonenumbers.parse(
          tourney.contact_phone, 'US'),
          phonenumbers.PhoneNumberFormat.NATIONAL)
  context = {'tourney': tourney}
  return render(request, 'find/detail.html', context)
