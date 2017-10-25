from django.conf.urls import url

from .views import signup, signin, signout, profile, facebook_login

urlpatterns = [
    url(r'^members/signup/$', signup, name='signup'),
    url(r'^members/login/$', signin, name='signin'),
    url(r'^members/logout/$', signout, name='signout'),
    url(r'^members/(?P<user_pk>\d+)/profile/$', profile, name='profile'),
    url(r'^members/facebook-login/$', facebook_login, name='facebook_login')
]
