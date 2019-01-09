from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^first/',views.first,name='first'),
    #path('first', views.first, name='first'),
  
]