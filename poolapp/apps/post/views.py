from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

from poolapp.apps.post.models import Name
from poolapp.apps.post.forms import NameForm

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
