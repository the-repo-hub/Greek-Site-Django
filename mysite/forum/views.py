from django.shortcuts import render
from forum.models import *
# Create your views here.
from django.views.generic import ListView, DetailView


class ThemesList(ListView):
    model = Theme
    context_object_name = 'themes'
    template_name = 'forum/themes_list.html'

class ViewTheme(DetailView):
    model = Theme
    context_object_name = 'theme' # context dictionary
    template_name = 'forum/theme.html'

"""def post_page(r, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(r, 'forum/post.html', context=context)"""

