from pprint import pprint

import requests
from django.contrib.auth import logout, get_user_model, login
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from config import settings
from config.settings import FACEBOOK_APP_ID
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
        'facebook_app_id': FACEBOOK_APP_ID,
    }
    return render(request, 'member/login.html', context)


def signout(request):
    logout(request)
    return redirect('post:post_list')


@login_required
def profile(request):
    return HttpResponse(f'User profile page {request.user}')


def facebook_login(request):
    app_id = settings.FACEBOOK_APP_ID
    app_secret_code = settings.FACEBOOK_APP_SECRET_CODE
    code = request.GET.get('code')

    # 사용자가 페이스북에 로그인하기 위한 링크에 있던 'redirect_url' GET 파라미터의 값과 동일한 값
    redirect_uri = '{scheme}://{host}{relative_url}'.format(
        scheme=request.scheme,
        host=request.META['HTTP_HOST'],
        relative_url=reverse('member:facebook_login'),
    )
    print('redirect_uri:', redirect_uri)
    url_access_token = 'https://graph.facebook.com/v2.10/oauth/access_token'
    params_access_token = {
        'client_id': app_id,
        'redirect_uri': redirect_uri,
        'client_secret': app_secret_code,
        'code': code,
    }
    response = requests.get(url_access_token, params_access_token)
    result = response.json()
    pprint(result)
    return HttpResponse(result)
