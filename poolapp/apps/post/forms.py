from django import forms
from django.forms import ModelForm 
from poolapp.apps.post.models import *
from django.contrib.admin import widgets

class TourneyForm(ModelForm):

  class Meta:
    model = Tourney
    fields = (
      'state',
      'pool_hall',
      'game',
      'field_size',
      'date',
      'fee',
      'added_money',
      'tourney_format',
      'contact_name',
      'contact_phone',
      'contact_email',
      'start_time',
      'end_time',
      'title',
      'adtnl_info'
    )
    widgets = {
            'adtnl_info': forms.Textarea,
            'date': forms.TextInput(attrs={'class':'datepicker'}),
            'start_time': forms.TextInput(attrs={'class':'timepicker', 
                'autocomplete':'off'}),
            'end_time': forms.TextInput(attrs={'class':'timepicker', 
                'autocomplete':'off'}),
            'contact_phone': forms.TextInput(attrs={'class':'phone'}),
        }
