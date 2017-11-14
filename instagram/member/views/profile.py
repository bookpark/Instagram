from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

User = get_user_model()


@login_required
def profile(request, user_pk):
    target_user = User.objects.get(pk=user_pk)
    context = {
        'target_user': target_user,
    }
    return render(request, 'member/profile.html', context)
