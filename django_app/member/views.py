from django.contrib.auth import authenticate, login as django_login, logout as django_logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .froms import LoginForm


def login(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(
        #     request,
        #     username=username,
        #     password=password,
        # )
        # if user is not None:
        #     django_login(request, user)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('post:post_list')
        else:
            return HttpResponse('login Error')
    else:
        # 만약 이미 로그인 된 상태일 경우에는 post_list로 redirect
        if request.user.is_authenticated:
            return redirect('post:post_list')
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'member/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already exist')
        if password1 != password2:
            return HttpResponse('PassWord Check Error')

        created_user = User.objects.create_user(
            username=username,
            password=password1,
        )
        django_login(request, created_user)
        return redirect('post:post_list')
    else:
        return render(request, 'member/signup.html')
