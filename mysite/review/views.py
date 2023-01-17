from django.shortcuts import render
from django.contrib.auth import login, authenticate
from singuplogin.forms import NewUserForm
# Create your views here.


def main_page(r):
    if r.user.is_authenticated:
        print('Yes, it is!')
    else:
        print('No!')
    return render(r, 'index.html')

def declinations(r):
    return render(r, 'declination.html')

def times(r):
    return render(r, 'tenses.html')

def cases(r):
    return render(r, 'cases.html')

def phrases(r):
    return render(r, 'phrases.html')

def ipersidelikos(r):
    return render(r, 'texts/tenses/Υπερσυντέλικος.html')

def aoristos(r):
    return render(r, 'texts/tenses/Αόριστος.html')

def paratatikos(r):
    return render(r, 'texts/tenses/Παρατατικός.html')

def enestotas(r):
    return render(r, 'texts/tenses/Ενεστότας.html')

def parakimenos(r):
    return render(r, 'texts/tenses/Παρακείμενος.html')

def melonas_stigmiaos(r):
    return render(r, 'texts/tenses/Μέλλοντας_στιγμιαίος.html')

def melonas_diarkias(r):
    return render(r, 'texts/tenses/Μέλλοντας_διαρκείας.html')

def melonas_sidelemenos(r):
    return render(r, 'texts/tenses/Μέλλοντας_συντελεσμένος.html')