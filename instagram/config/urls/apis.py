from django.conf.urls import url, include

urlpatterns = [
    url(r'^members/', include('member.urls.apis', namespace='member')),
    url(r'^posts/', include('post.urls.apis', namespace='post')),
    url(r'^sms/', include('sms.urls', namespace='sms')),
]
