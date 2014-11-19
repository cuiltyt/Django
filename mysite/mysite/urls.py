from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^track/', include('track.urls', namespace="track")),
    url(r'^admin/', include(admin.site.urls)),
)
