from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('declinations/', declinations),
    path('tenses/', times),
    path('cases/', cases),
    path('phrases/', phrases),
    path('tenses/υπερσυντέλικος/', ipersidelikos),
]