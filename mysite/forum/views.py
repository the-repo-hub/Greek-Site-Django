from django.shortcuts import render
from forum.models import *
from forum.forms import *
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView


class ThemesList(ListView):
    model = Theme
    context_object_name = 'themes'
    template_name = 'forum/themes_list.html'

def in_theme(r, pk):
    theme = Theme.objects.get(pk=pk)
    posts = Post.objects.filter(theme=theme)
    context = {'theme': theme, 'posts': posts, 'author': r.user}
    return render(r, 'forum/posts_list.html', context=context)

class AddTheme(CreateView):
    form_class = ThemeForm
    template_name = 'forum/add_theme.html'


"""def add_theme(r):
    form = ThemeForm()
    if r.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(r, 'forum/add_theme.html', context=context)
"""