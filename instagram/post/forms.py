from django import forms

# from .models import Comment, Post

__all__ = (
    'PostForm',
    'CommentForm',
)


class PostForm(forms.Form):
    photo = forms.ImageField()
    # description = forms.CharField(widget=forms.Textarea)

# class Meta:
#     model = Post
#     fields = (
#         'photo',
#     )


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea,
    )
