from django.shortcuts import render
from forum.models import Post
# Create your views here.

def forum_main_page(r):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(r, 'forum/forum.html', context=context)

def post_page(r, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(r, 'forum/post.html', context=context)