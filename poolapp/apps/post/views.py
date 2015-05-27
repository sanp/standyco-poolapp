from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

from poolapp.apps.post.models import Tourney
from poolapp.apps.post.forms import TourneyForm

def tourney_form_upload(request):
  if request.method == 'GET':
    form = TourneyForm()
  else:
    # A POST request: Handle Form Upload
    form = TourneyForm(request.POST) # Bind data from request.POST into a PostForm
 
    # If data is valid, proceeds to create a new post and redirect the user
    if form.is_valid():

      state = form.cleaned_data['state']
      pool_hall = form.cleaned_data['pool_hall']
      game = form.cleaned_data['game']
      game_other = form.cleaned_data['game_other']
      field_size = form.cleaned_data['field_size']
      date = form.cleaned_data['date']
      end_date = form.cleaned_data['end_date']
      fee = form.cleaned_data['fee']
      added_money = form.cleaned_data['added_money']
      added_money_based_on_full_field = form.cleaned_data['added_money_based_on_full_field']
      tourney_format = form.cleaned_data['tourney_format']
      contact_name = form.cleaned_data['contact_name']
      contact_phone = form.cleaned_data['contact_phone']
      contact_email = form.cleaned_data['contact_email']
      start_time = form.cleaned_data['start_time']
      title = form.cleaned_data['title']
      has_calcutta = form.cleaned_data['has_calcutta']
      race_to_single = form.cleaned_data['race_to_single']
      race_to_a = form.cleaned_data['race_to_a']
      race_to_b = form.cleaned_data['race_to_b']
      green_fees_included = form.cleaned_data['green_fees_included']
      green_fees = form.cleaned_data['green_fees']
      adtnl_info = form.cleaned_data['adtnl_info']

      tourney = Tourney.objects.create(
                  state = state,
                  pool_hall = pool_hall,
                  game = game,
                  game_other = game_other,
                  field_size = field_size,
                  date = date,
                  end_date = end_date,
                  fee = fee,
                  added_money = added_money,
                  tourney_format = tourney_format,
                  contact_name = contact_name,
                  contact_phone = contact_phone,
                  contact_email = contact_email,
                  start_time = start_time,
                  title = title,
                  has_calcutta = has_calcutta,
                  race_to_single = race_to_single,
                  race_to_a = race_to_a,
                  race_to_b = race_to_b,
                  green_fees_included = green_fees_included,
                  green_fees = green_fees,
                  added_money_based_on_full_field = 
                    added_money_based_on_full_field,
                  adtnl_info = adtnl_info,
                )

      return render(request, 'post/success.html', {})
 
  return render(request, 'post/tourney_form_upload.html', {
    'form': form,
  })
