from django.conf.urls import patterns, url

from poolapp.apps.post import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^names$', views.detail, name='detail'),

  # Posting content
#   url(r'^name/(?P<name_id>\d+)/name_detail.html$', views.name_detail, 
#     name='name_detail'),
  # Link the view views.post_upload to URL post/upload.html
  url(r'^name/upload.html$', views.name_upload, name='name_upload'),

)
