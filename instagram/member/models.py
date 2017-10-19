from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models


class UserManager(DjangoUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(age=30, *args, **kwargs)


class User(AbstractUser):
    # FileField는 문자열 필드라 null=True가 들어가지 않는다
    img_profile = models.ImageField(
        upload_to='user',
        blank=True,
    )
    age = models.IntegerField()

    objects = UserManager()

    # REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['age']
