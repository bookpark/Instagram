from django.shortcuts import render, redirect

from .forms import CommentForm
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
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        Post.objects.create(photo=photo)
        return redirect('post_list')
    return render(request, 'post/post_upload.html')


def post_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail')
        else:
            form = CommentForm()
        return render(request, 'post/post_comment.html', {
            'form': form,
        })
