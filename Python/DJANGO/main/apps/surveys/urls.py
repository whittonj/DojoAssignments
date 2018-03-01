from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.display),
    url(r'^surveys/$', views.display),
    url(r'^surveys/create/$', views.create),
]
