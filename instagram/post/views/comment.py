from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404

from ..forms import CommentForm
from ..models import Post, Comment

__all__ = [
    'post_comment',
    'comment_delete',
]

def post_comment(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('member:signin')
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # post와 연결
            comment.post = post
            comment.save()
            # 생성 후 Post의 detail 화면으로 이동
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('post:post_detail', post_pk=post_pk)


def comment_delete(request, comment_pk):
    next_path = request.GET.get('next', '').strip()
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST' and request.user == comment.author:
        comment.delete()
        if next_path:
            return redirect(next_path)
        return redirect('post:post_list')
    raise PermissionDenied
