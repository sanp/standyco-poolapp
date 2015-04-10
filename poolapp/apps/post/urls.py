from django.conf.urls import patterns, url

from poolapp.apps.post import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
