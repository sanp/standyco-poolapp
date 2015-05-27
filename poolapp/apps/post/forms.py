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
      'game_other',
      'tourney_format_other',
      'field_size_other',
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
            'title': forms.TextInput(attrs={'placeholder':'My Awesome Tournament'}),
            'pool_hall': forms.TextInput(attrs={'placeholder':'My Awesome Pool Hall'}),
            'game_other': forms.TextInput(attrs={
                'placeholder':'Another game type'
              }),
            'tourney_format_other': forms.TextInput(attrs={
                'placeholder':'Another format'
              }),
            'field_size_other': forms.TextInput(attrs={
                'placeholder':'Another field size'
              }),
            'fee': forms.TextInput(attrs={'placeholder':'$20'}),
            'added_money': forms.TextInput(attrs={'placeholder':'$2,000'}),
            'date': forms.TextInput(attrs={
                'class':'datepicker',
                'placeholder': 'mm/dd/yyyy'
              }),
            'start_time': forms.TextInput(attrs={
                'class':'timepicker', 
                'autocomplete':'off',
                'placeholder': 'hh:mm'
              }),
            'end_time': forms.TextInput(attrs={
                'class':'timepicker', 
                'autocomplete':'off',
                'placeholder': 'hh:mm'
              }),
            'contact_phone': forms.TextInput(attrs={
                'class':'phone',
                'placeholder': '(201) 555-5555'
              }),
            'contact_name': forms.TextInput(attrs={'placeholder':'Jane Smith'}),
            'contact_email': forms.TextInput(attrs={'placeholder':'jane@smithco.com'}),
            'adtnl_info': forms.Textarea(attrs={
                'rows': '3',
                'placeholder':'Feel free to give any extra information you want.'
              }),
        }
