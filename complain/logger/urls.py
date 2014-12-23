from django.conf.urls import patterns, url

from complain import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
