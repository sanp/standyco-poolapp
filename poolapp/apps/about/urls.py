from django.conf.urls import patterns, url

from poolapp.apps.about import views

urlpatterns = patterns('',
    # ex: /about/
    url(r'^$', views.index, name='index'),
    # ex: /about/contact
    url(r'contact/$', views.contact, name='contact'),
    # ex: /about/thanks
    url(r'contact/thanks/$', views.thanks, name='thanks'),
)
