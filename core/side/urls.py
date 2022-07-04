from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
      #path('', home_view, name='home'),   
      #path('rest-auth/', include('rest_auth.urls')),

    path('s/',TestView.as_view(), name='test'), path('api/token/',obtain_auth_token, name='obtain-token'),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework' ))]
  