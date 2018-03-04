from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^users/$', views.index), 
    url(r'^users/create$', views.create),
    url(r'^update/(?P<user_no>\d+)/$', views.update),
    url(r'^users/new/$', views.new),
    url(r'^users/(?P<user_no>\d+)/$', views.results),
    url(r'^users/(?P<user_no>\d+)/edit/$', views.edit)
    ]