from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^logger', include('logger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
