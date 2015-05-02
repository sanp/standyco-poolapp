from django.conf.urls import patterns, url
from poolapp.apps.post import views

from poolapp.apps.post.preview import TourneyFormPreview
from poolapp.apps.post.forms import TourneyForm
from django import forms

urlpatterns = patterns('',
  url(r'^$', TourneyFormPreview(TourneyForm)),
)
