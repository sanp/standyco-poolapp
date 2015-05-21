from poolapp.apps.about.forms import ContactForm

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def index(request):
  return render_to_response('about/index.html', context_instance=RequestContext(request))

def contact(request):

  if request.method == 'GET':
    form = ContactForm()
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message_top = 'Sender Name: %s\nSender Email: %s\n\n------------------\n\n' % (name, email)
      message = message_top + form.cleaned_data['message']
      try:
        send_mail('Pool App - %s' % name, message, email, ['standyco.inc@gmail.com'])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      return redirect('thanks')
  return render(request, 'about/contact.html', {'form': form})

def thanks(request):
  return render_to_response('about/thanks.html', context_instance=RequestContext(request))
