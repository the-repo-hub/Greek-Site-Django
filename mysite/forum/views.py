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
    context_object_name = 'new_theme'
    template_name = 'forum/add_theme.html'

"""def post_page(r, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(r, 'forum/post.html', context=context)"""

