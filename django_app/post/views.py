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


def post_create(request):
    if request.method == 'POST':
        user = User.objects.first()
        post = Post.objects.create(
            author=user,
            photo=request.FILES['file']  # 'file'은 POST 요청시 input[type="file"]이 가진 name 속성
        )
        comment_string = request.POST.get('comment', '')
        if comment_string:
            post.comment_set.create(
                author=user,
                content=comment_string,
            )
        else:
            pass
        return redirect('post:post_detail', post_pk=post.pk)
    else:
        return render(request, 'post/post_create.html')


def post_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('post:post_list')


