from django.contrib.auth import get_user_model
from django.shortcuts import redirect

User = get_user_model()


def follow_toggle(request, user_pk):
    if request.method == 'POST':
        followee = User.objects.get(pk=user_pk)
        following = request.user
        following.follow_toggle(followee)
        return redirect('member:profile', user_pk=user_pk)
