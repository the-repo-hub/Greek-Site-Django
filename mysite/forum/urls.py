from django.contrib import admin
from django.urls import path, include
from forum.views import *

urlpatterns = [
    path('', ThemesList.as_view(), name='themes_list'),
    path('<int:pk>', ViewTheme.as_view(), name='theme'),
]
