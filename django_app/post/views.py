from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)
