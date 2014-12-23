from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^complain', include('complain.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
