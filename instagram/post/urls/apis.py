from django.conf.urls import url

from .. import apis

urlpatterns = [
    url(r'^$', apis.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', apis.PostDetail.as_view(), name='post-detail')
]
