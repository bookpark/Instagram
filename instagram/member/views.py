from django.contrib.auth import logout, get_user_model
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.forms import SignupForm, SigninForm

# User model을 가져올 때는 이 함수를 써서 import 하는 것을 추천
User = get_user_model()


# Custom validation
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.signup()
            return redirect('signin')
    else:
        form = SignupForm
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def signin(request):
    """
    is_valid()에서 주어진 username/password를 사용한 authenticate 실행
    성공시 login(request) method를 사용할 수 있음
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.signin(request)
            return redirect('post_list')
        else:
            return HttpResponse('Login failed')
    else:
        return render(request, 'member/login.html')


def signout(request):
    logout(request)
    return redirect('post_list')
