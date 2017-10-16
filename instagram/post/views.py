from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_upload(request):
    if request.method == 'POST':
        # POST 요청의 경우 PostForm 인스턴스 생성과정에서 request.POST, request.FILES 사용
        form = PostForm(request.POST, request.FILES)
        # Form 생성 과정에서 전달된 데이터들이 Form의 모든 field들에 유효한지 검사
        if form.is_valid():
            # 유효할 경우 Post 인스턴스를 생성 및 저장
            Post.objects.create(photo=form.cleaned_data['photo'])
        return redirect('post_list')
    else:
        # GET 요청의 경우 빈 PostForm 인스턴스를 생성해서 템플릿에 전달
        form = PostForm()
        # GET 요청에선 이 부분이 무조건 실행
        # POST 요청에선 form.is_valid()를 통과하지 못하면 이 부분이 실행
        context = {
            'form': form
        }
    return render(request, 'post/post_upload.html', context)


# def post_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = Post.objects.get(comment=comment)
#             comment.save()
#             return redirect('post_detail')
#         else:
#             form = CommentForm()
#         return render(request, 'post/post_comment.html', {
#             'form': form,
#         })


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')
    return HttpResponse('Permission Denied', status=403)
