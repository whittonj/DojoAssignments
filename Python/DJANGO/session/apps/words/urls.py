from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^create$', views.create),
    url(r'^results$', views.results)
    ]