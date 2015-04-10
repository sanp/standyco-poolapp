from django.conf.urls import patterns, url

from poolapp.apps.forums import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
