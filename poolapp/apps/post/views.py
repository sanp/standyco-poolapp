from django.shortcuts import render_to_response
from django.template import RequestContext
#  
# def index(request):
#     return render_to_response('post/index.html', context_instance=RequestContext(request))

from django.shortcuts import render
from django.http import HttpResponseRedirect

from poolapp.apps.post.models import Name

# def index(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
# 
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
# 
#     return render(request, 'post/index.html', {'form': form})

def index(request):
  return render(request, 'post/index.html', {})

def detail(request):
  name_list = Name.objects.all()
  context = {'name_list': name_list}
  return render(request, 'post/detail.html', context)


###

# http://www.pythoncentral.io/writing-views-to-upload-posts-for-your-first-python-django-application/
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
  
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
