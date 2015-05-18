from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'poolapp.apps.home.views.index', name='home'),
    url(r'^tournaments/post/', include('poolapp.apps.post.urls')),
    url(r'^tournaments/find/', include('poolapp.apps.find.urls')),
    url(r'^forums/', include('poolapp.apps.forums.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
