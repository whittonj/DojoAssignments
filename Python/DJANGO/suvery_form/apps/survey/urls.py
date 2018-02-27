from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed!
    url(r'^survey/create$', views.create),
    url(r'^survey/results$', views.results)
    ]