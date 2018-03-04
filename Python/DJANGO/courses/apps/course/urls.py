from django.conf.urls import url, include
from . import views          
urlpatterns = [
    url(r'^$', views.index),    
    url(r'^create$', views.create),
    #url(r'^course/(?P<user_no>\d+)/$', views.update),
    url(r'^course/(?P<user_no>\d+)/$', views.results),
    url(r'^destroy/(?P<user_no>\d+)/$', views.destroy)
    ]