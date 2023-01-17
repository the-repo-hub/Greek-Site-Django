from django.shortcuts import render

# Create your views here.

def forum_main_page(r):
    return render(r, 'forum/forum.html')
