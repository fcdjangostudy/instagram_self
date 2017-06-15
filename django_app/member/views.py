from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            django_login(request, user)
            return redirect('post:post_list')
        else:
            return HttpResponse('login Error')
    else:
        # 만약 이미 로그인 된 상태일 경우에는 post_list로 redirect
        if request.user.is_authenticated:
            return redirect('post:post_list')
        return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 is not password2:
            return redirect('member:signup')
        else:
            for user in User.objects.all():
                if username == user.username:
                    return redirect('member:signup')
        created_user = User.objects.create(username=username)
        created_user.set_password(password1)
        return redirect('post:post_list')
    else:
        return render(request, 'member/signup.html')
