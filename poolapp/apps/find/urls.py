from django.conf.urls import patterns, url

from poolapp.apps.find import views

urlpatterns = patterns('',
    # ex: /tournaments/find/
    url(r'^$', views.index, name='index'),
    # ex: /tournaments/find/state/IL/
    url(r'^state/(?P<state_id>\w+)/$', views.state, name='state'),
    # Make a url for tournament in state
    # ex: /tournaments/find/state/IL/<tourney_id>
    url(r'^state/(\w+)/(?P<tourney_id>\d+)/$', 
        views.tourney, name='tourney'),
)
