from django.conf.urls import patterns, url

from poolapp.apps.post import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^names$', views.detail, name='detail'),

  # Posting content
  # Name
  # Manually - not using the forms.py approach
  url(r'^name/upload.html$', views.name_upload, name='name_upload'),
  # Using the forms.py approach
  url(r'^name/name_form_upload.html$',
        views.name_form_upload, name='name_form_upload'),

  # Tourney
  # Using the forms.py approach
  url(r'^name/name_form_upload.html$',
        views.name_form_upload, name='name_form_upload'),

)
