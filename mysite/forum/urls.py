from django.contrib import admin
from django.urls import path, include
from forum.views import *

urlpatterns = [
    path('', forum_main_page),
    path('<int:pk>', post_page)
]
