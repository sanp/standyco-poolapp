from django.db import models
from django import forms
from django.core.validators import RegexValidator
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

class Tourney(models.Model):

  # Choices

  # Game
  EIGHT_BALL = 0
  NINE_BALL = 1
  TEN_BALL = 2
  ONE_POCKET = 3
  STRAIGHT_POOL = 4
  BANK_POOL = 5
  OTHER_GAME = 6
  GAME_CHOICES = (
      (EIGHT_BALL, '8-ball'),
      (NINE_BALL, '9-ball'),
      (TEN_BALL, '10-ball'),
      (ONE_POCKET, 'One-pocket'),
      (STRAIGHT_POOL, 'Straight Pool'),
      (BANK_POOL, 'Bank Pool'),
      (OTHER_GAME, 'Other')
    )

  # Field Size
  TWO_P = 0
  FOUR_P = 1
  SIXT_P = 2
  THIR_P = 3
  SIXT_P = 4
  FIELD_SIZE_CHOICES = (
      (TWO_P, '2 man'),
      (FOUR_P, '4 players'),
      (SIXT_P, '16 players'),
      (THIR_P, '32 players'),
      (SIXT_P, '64 players')
    )

  # Tourney Format
  SINGLE = 0
  DOUBLE = 1
  OTHER_FORMAT = 2
  TOURNEY_FORMAT_CHOICES = (
      (SINGLE, 'Single elimination'),
      (DOUBLE, 'Double elimination'),
      (OTHER_FORMAT, 'Other')
    )

  # Fields
  tourney_id = models.AutoField(primary_key=True)
  state = USStateField(choices=STATE_CHOICES, default='IL')
  # TODO: add cities
  # TODO: add sub-city regions
  pool_hall = models.CharField(max_length=200)
  game = models.IntegerField(choices=GAME_CHOICES, default=EIGHT_BALL)
  field_size = models.IntegerField(choices=FIELD_SIZE_CHOICES,
      default=THIR_P)
  date = models.DateField('Tournament Date')
  fee = models.DecimalField(max_digits=6, decimal_places=2)
  added_money = models.DecimalField(max_digits=6, decimal_places=2)
  tourney_format = models.IntegerField(choices=TOURNEY_FORMAT_CHOICES, 
      default=SINGLE)
  contact_name = models.CharField(max_length=200)

  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
      message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  contact_phone = models.CharField(max_length=15, validators=[phone_regex], 
      blank=True, null=True) # validators should be a list

  contact_email = models.EmailField(max_length=100)
  start_time = models.TimeField('Start time', blank=False)
  end_time = models.TimeField('End time', blank=True, null=True) # End time optional
  title = models.CharField(max_length=70)
  adtnl_info = models.CharField(max_length=1000, blank=True, null=True)

  def __str__(self):              # __unicode__ on Python 2
    return self.title
