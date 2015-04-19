from django import forms
from django.forms import ModelForm 
from poolapp.apps.post.models import *
from django.contrib.admin import widgets

class NameForm(ModelForm):
  class Meta:
    model = Name

class TourneyForm(ModelForm):

  class Meta:
    model = Tourney
