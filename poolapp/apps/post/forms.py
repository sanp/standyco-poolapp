from django.forms import ModelForm
from poolapp.apps.post.models import *

class NameForm(ModelForm):
  class Meta:
    model = Name

class TourneyForm(ModelForm):
  class Meta:
    model = Tourney
