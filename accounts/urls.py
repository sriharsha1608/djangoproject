from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


from . import views 

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('materials', views.materials, name="materials"),
    
]