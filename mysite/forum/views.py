from django.shortcuts import render
from forum.models import Post
# Create your views here.
from django.views.generic import ListView, DetailView


def forum_main_page(r):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(r, 'forum/forum.html', context=context)

class ViewPost(DetailView):
    model = Post
    context_object_name = 'post' # context dictionary
    template_name = 'forum/post.html'

"""def post_page(r, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(r, 'forum/post.html', context=context)"""

