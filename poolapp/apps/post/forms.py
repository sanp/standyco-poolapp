from django import forms
from django.forms import ModelForm 
from poolapp.apps.post.models import *
from django.contrib.admin import widgets

class TourneyForm(ModelForm):

  class Meta:
    model = Tourney
    widgets = {
            'adtnl_info': forms.Textarea,
            'date': forms.TextInput(attrs={'class':'datepicker'}),
            'start_time': forms.TextInput(attrs={'class':'timepicker', 
                'autocomplete':'off'}),
            'end_time': forms.TextInput(attrs={'class':'timepicker', 
                'autocomplete':'off'}),
        }
