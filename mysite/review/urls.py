from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('declinations/', declinations),
    path('tenses/', times),
    path('cases/', cases),
    path('phrases/', phrases),
    path('tenses/υπερσυντέλικος/', ipersidelikos),
    path('tenses/αόριστος/', aoristos),
    path('tenses/παρατατικός/', paratatikos),
    path('tenses/ενεστότας/', enestotas),
    path('tenses/παρακείμενος/', parakimenos),
    path('tenses/μέλλοντας_στιγμιαίος/', melonas_stigmiaos),
    path('tenses/μέλλοντας_διαρκείας/', melonas_diarkias),
    path('tenses/μέλλοντας_συντελεσμένος/', melonas_sidelemenos),
]