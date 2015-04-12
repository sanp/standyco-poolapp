from django.shortcuts import render_to_response
from django.template import RequestContext
#  
# def index(request):
#     return render_to_response('post/index.html', context_instance=RequestContext(request))

from django.shortcuts import render
from django.http import HttpResponseRedirect

from poolapp.apps.post.forms import NameForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'post/index.html', {'form': form})
