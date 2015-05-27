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
      'end_date',
      'multiple_days',
      'fee',
      'added_money',
      'added_money_based_on_full_field',
      'tourney_format',
      'contact_name',
      'contact_phone',
      'contact_email',
      'start_time',
      'title',
      'has_calcutta',
      'race_to_single',
      'race_to_a',
      'race_to_b',
      'green_fees_included',
      'green_fees',
      'adtnl_info'
    )
    widgets = {
            'title': forms.TextInput(attrs={'placeholder':'My Awesome Tournament'}),
            'has_calcutta': forms.RadioSelect,
            'multiple_days': forms.RadioSelect,
            'added_money_based_on_full_field': forms.RadioSelect,
            'green_fees_included': forms.RadioSelect,
            'green_fees': forms.TextInput(attrs={'placeholder':'$20'}),
            'race_to_single': forms.TextInput(attrs={'placeholder':'5'}),
            'race_to_a': forms.TextInput(attrs={'placeholder':'5'}),
            'race_to_b': forms.TextInput(attrs={'placeholder':'3'}),
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
            'end_date': forms.TextInput(attrs={
                'class':'datepicker',
                'placeholder': 'mm/dd/yyyy'
              }),
            'start_time': forms.TextInput(attrs={
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
