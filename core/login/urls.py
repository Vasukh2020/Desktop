from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',home , name='home'),
     path('register/',register, name='register'),
      path('api/token/',obtain_auth_token, name='obtain-token'),
     path('login/',login, name='login'), 
          path('api/',api_list_view, name='api'), 
           path('api2/',api2_list_view, name='api2'), 

     #path('<int:pk>/detail/',detail, name='detail'),

        path('api-auth/', include('rest_framework.urls', namespace='rest_framework' ))]
  