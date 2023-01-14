from django.shortcuts import render
# Create your views here.


def main_page(r):
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
    return render(r, 'tenses/Υπερσυντέλικος.html')

