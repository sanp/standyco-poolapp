from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.core.validators import RegexValidator
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

from poolapp.apps.post.models import Name, Tourney
from poolapp.apps.post.forms import NameForm, TourneyForm

def index(request):
  return render(request, 'post/index.html', {})

def detail(request):
  name_list = Name.objects.all()
  context = {'name_list': name_list}
  return render(request, 'post/detail.html', context)

# http://www.pythoncentral.io/writing-views-to-upload-posts-for-your-first-python-django-application/
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
  
# Add the following function to the end of myblog/views.py
def name_upload(request):
  if request.method == 'GET':
    return render(request, 'post/name_upload.html', {})
  elif request.method == 'POST':
    name = Name.objects.create(your_name=request.POST['name'],
        your_address=request.POST['address'])
    # No need to call post.save() at this point -- it's already saved.
#     return HttpResponseRedirect(reverse('post/detail'))
    return render(request, 'post/success.html', {})

### Using Forms

def name_form_upload(request):
  if request.method == 'GET':
    form = NameForm()
  else:
    # A POST request: Handle Form Upload
    form = NameForm(request.POST) # Bind data from request.POST into a PostForm
 
    # If data is valid, proceeds to create a new post and redirect the user
    if form.is_valid():
      your_name = form.cleaned_data['your_name']
      your_address = form.cleaned_data['your_address']
      name = Name.objects.create(your_name=your_name,
                     your_address=your_address)
      return render(request, 'post/success.html', {})
 
  return render(request, 'post/name_form_upload.html', {
    'form': form,
  })

### Tourney Form Upload

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
