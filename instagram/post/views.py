from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, CommentForm
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'form': comment_form,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    context = {
        'post': post,
        'form': comment_form,
    }
    return render(request, 'post/post_detail.html', context)


def post_upload(request):
    if not request.user.is_authenticated:
        return redirect('member:signin')
    if request.method == 'POST':
        # POST 요청의 경우 PostForm 인스턴스 생성과정에서 request.POST, request.FILES 사용
        form = PostForm(request.POST, request.FILES)
        # Form 생성 과정에서 전달된 데이터들이 Form의 모든 field들에 유효한지 검사
        if form.is_valid():
            # 1. 커스텀 메서드 사용
            # form.save(author=request.user)

            # 2. 기존 Django의 ModelForm 방식 사용
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_list')
    else:
        # GET 요청의 경우 빈 PostForm 인스턴스를 생성해서 템플릿에 전달
        form = PostForm()
        # GET 요청에선 이 부분이 무조건 실행
        # POST 요청에선 form.is_valid()를 통과하지 못하면 이 부분이 실행
    context = {
        'form': form,
    }
    return render(request, 'post/post_upload.html', context)


def post_comment(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('member:signin')
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                content=form.cleaned_data['content'],
            )
            # 생성 후 Post의 detail 화면으로 이동
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('post:post_detail', post_pk=post_pk)


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST' and request.user == post.author:
        post.delete()
        return redirect('post:post_list')
    raise PermissionDenied


def comment_delete(request, comment_pk):
    next_path = request.GET.get('next', '').strip()
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST' and request.user == comment.author:
        comment.delete()
        if next_path:
            return redirect(next_path)
        return redirect('post:post_list')
    raise PermissionDenied
