from django.conf.urls import url
from . import views          
urlpatterns = [
    #url(r'^$', views.index),   
    url(r'^books/add/$', views.create_book),
    #url(r'^books/(?P<book_no>\d+)/$', views.newbook)
    #url(r'^users/(?P<user_no>\d+)/$', views.results),
    url(r'^newbook$', views.newbook),
    #url(r'^login$', views.login),
    ]