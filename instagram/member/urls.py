from django.conf.urls import url

from .views import signup, signin, signout

urlpatterns = [
    url(r'^members/signup/$', signup, name='signup'),
    url(r'^members/login/$', signin, name='signin'),
    url(r'^members/logout/$', signout, name='signout'),
]