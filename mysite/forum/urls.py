from django.urls import path
from forum.views import *

urlpatterns = [
    path('', ThemesList.as_view(), name='themes_list'),
    path('<int:pk>', in_theme, name='theme'),
    path('add_theme/', AddTheme.as_view(), name='add_theme')
]
