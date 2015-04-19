from django.conf.urls import patterns, url

from poolapp.apps.post import views

urlpatterns = patterns('',
  url(r'^$', views.tourney_form_upload, name='tourney_form_upload'),
)
