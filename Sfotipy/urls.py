from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from artists.views import ArtistDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\W]+)', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view())



)

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)
