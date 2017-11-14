from django.conf.urls import url

from .. import views

urlpatterns = [
    # Post
    url(r'^', views.post_list, name='post_list'),
    url(r'^upload/$', views.post_upload, name='post_upload'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^(?P<post_pk>\d+)/like-toggle$', views.post_like_toggle, name='post_like_toggle'),

    # Comment
    url(r'^(?P<post_pk>\d+)/comments/add/', views.post_comment, name='post_comment'),
    url(r'^(?P<comment_pk>\d+)/comments/delete/', views.comment_delete, name='comment_delete'),
]
