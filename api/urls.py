from django.urls import path
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^first/',csrf_exempt(views.first),name='first'),
    #path('first', views.first, name='first'),
  
]