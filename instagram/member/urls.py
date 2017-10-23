from django.conf.urls import url

from .views import signup, signin, signout, profile

urlpatterns = [
    url(r'^members/signup/$', signup, name='signup'),
    url(r'^members/login/$', signin, name='signin'),
    url(r'^members/logout/$', signout, name='signout'),
    url(r'^members/profile/$', profile, name='profile'),
]