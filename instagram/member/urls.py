from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.signin, name='signin'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^(?P<user_pk>\d+)/profile/$', views.profile, name='profile'),
    url(r'^facebook-login/$', views.facebook_login, name='facebook_login'),
    url(r'^(?P<user_pk>\d+)/follow-toggle$', views.follow_toggle, name='follow_toggle'),
]
