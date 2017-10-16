from django.conf.urls import url

from .views import signup

urlpatterns = [
    url(r'^members/signup/$', signup, name='signup'),
]