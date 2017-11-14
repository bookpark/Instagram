from django.conf.urls import url

from .. import apis

urlpatterns = [
    url(r'^login/$', apis.Login.as_view(), name='api-login'),
    url(r'^signup/$', apis.Signup.as_view(), name='api-signup'),
    url(r'^facebook-login/$', apis.FacebookLogin.as_view(), name='facebook-login'),
]
