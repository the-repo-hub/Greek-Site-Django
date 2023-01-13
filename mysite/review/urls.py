from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('declinations/', declinations),
    path('times/', times),
    path('cases/', cases),
    path('phrases/', phrases)
]