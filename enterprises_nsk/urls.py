
from django.contrib import admin
from django.urls import path, include

from enterprises_nsk import views

urlpatterns = [
    path('', views.index, name='home'),
]
