from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'poolapp.apps.home.views.index', name='home'),
    url(r'^tournaments/post/', include('poolapp.apps.post.urls')),
    url(r'^tournaments/find/', include('poolapp.apps.find.urls')),
    url(r'^forums/', include('poolapp.apps.forums.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='%s/poolapp/img/favicon.ico' %
      settings.STATIC_URL)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
