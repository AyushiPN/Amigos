from django.contrib import admin
from django.urls import path, include
from amigos_cafe import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('booking', views.booking, name="booking"),
    path('contact', views.contact, name="contact"),
    path('feature', views.feature, name="feature"),
    path('menu', views.menu, name="menu"),
    path('login', views.userlogin, name="login"),
    path('register', views.register, name="register"),
    path('signout', views.signout, name="signout"),
    
]