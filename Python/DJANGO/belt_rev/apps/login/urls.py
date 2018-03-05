from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^users/$', views.index), 
    url(r'^create$', views.create),
    url(r'^users/(?P<user_no>\d+)/$', views.results),
    url(r'^register/$', views.register),
    url(r'^login$', views.login),
    ]
