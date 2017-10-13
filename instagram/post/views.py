from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_upload(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        Post.objects.create(photo=photo)
        return redirect('post_list')
    return render(request, 'post/post_upload.html')


# def post_comment(request):
#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         Post.objects.create(comment=comment)
#         return redirect('post_list')
#     return render(request, 'post/post_list.html')