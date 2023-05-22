
from django.contrib import admin
from django.urls import path, include

from django_app import views

urlpatterns = [
    path('', views.index, name='main'),

    path('login/', views.login_f, name='login'),
    path('register/', views.register_f, name='register'),
    path('logout/', views.logout_f, name='logout'),

]
