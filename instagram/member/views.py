from django.contrib.auth import logout, get_user_model, login
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.forms import SignupForm, SigninForm

# User model을 가져올 때는 이 함수를 써서 import 하는 것을 추천
User = get_user_model()


# Custom validation
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:post_list')
    else:
        form = SignupForm
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def signin(request):
    next_path = request.GET.get('next')
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.signin(request)
            if next_path:
                return redirect(next_path)
            return redirect('post:post_list')
    else:
        form = SigninForm
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)


def signout(request):
    logout(request)
    return redirect('post:post_list')


@login_required
def profile(request):
    return HttpResponse(f'User profile page {request.user}')
