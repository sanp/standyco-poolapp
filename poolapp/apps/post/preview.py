from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect

from poolapp.apps.post.models import Tourney
from poolapp.apps.post.forms import TourneyForm

class TourneyFormPreview(FormPreview):

  form_template = 'post/tourney_form_upload.html'

  def done(self, request, cleaned_data):
    # Do something with the cleaned_data, then redirect
    # to a "success" page.
    return HttpResponseRedirect('/post/success')
