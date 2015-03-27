from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poolapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'poolapp.apps.home.views.index'),
    url(r'^tournaments/post/', 'poolapp.apps.post.views.index'),
    url(r'^tournaments/find/', 'poolapp.apps.find.views.index'),
    url(r'^forums/', 'poolapp.apps.forums.views.index'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
