from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from member.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
        # return redirect('member/signup.html')
        return HttpResponse(f'{user.username}, {user.password}')
    else:
        form = SignupForm
        context = {
            'form': form,
        }
    return render(request, 'member/signup.html', context)
