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
      field_size = form.cleaned_data['field_size']
      date = form.cleaned_data['date']
      fee = form.cleaned_data['fee']
      added_money = form.cleaned_data['added_money']
      tourney_format = form.cleaned_data['tourney_format']
      contact_name = form.cleaned_data['contact_name']
      contact_phone = form.cleaned_data['contact_phone']
      contact_email = form.cleaned_data['contact_email']
      start_time = form.cleaned_data['start_time']
      end_time = form.cleaned_data['end_time']
      title = form.cleaned_data['title']
      adtnl_info = form.cleaned_data['adtnl_info']

#       state = 'IL'
#       pool_hall = 'My hall'
#       game = 0
#       field_size = 3
#       date = '2015-05-09'
#       fee = 22.00
#       added_money = 200.00
#       tourney_format = 1
#       contact_name = 'Steve'
#       contact_phone = '6319821234'
#       contact_email = form.cleaned_data['contact_email']
#       start_time = '18:00:00'
#       end_time = '22:00:00'
#       title = 'Auto gen tournament'
#       adtnl_info = 'Nothing'

      tourney = Tourney.objects.create(
                  state = state,
                  pool_hall = pool_hall,
                  game = game,
                  field_size = field_size,
                  date = date,
                  fee = fee,
                  added_money = added_money,
                  tourney_format = tourney_format,
                  contact_name = contact_name,
                  contact_phone = contact_phone,
                  contact_email = contact_email,
                  start_time = start_time,
                  end_time = end_time,
                  title = title,
                  adtnl_info = adtnl_info,
                )

      return render(request, 'post/success.html', {})
 
  return render(request, 'post/tourney_form_upload.html', {
    'form': form,
  })
