from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/$', views.index),
    #url(r'^blogs/?[0-9]+$', views.blog_number),
    url(r'^blogs/(?P<blog_no>\d+)/$', views.blog_number),
    url(r'^blogs/create/$', views.create),
    url(r'^blogs/new/$', views.new)
]
