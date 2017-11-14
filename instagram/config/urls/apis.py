from django.conf.urls import url, include

from utils.sms.apis import SendSMS

urlpatterns = [
    url(r'^members/', include('member.urls.apis', namespace='member')),
    url(r'^posts/', include('post.urls.apis', namespace='post')),
    url(r'^utils/sms/send/$', SendSMS.as_view(), name='send-sms'),
]
