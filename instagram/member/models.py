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
        verbose_name='프로필 사진',
    )
    age = models.IntegerField('나이')
    like_posts = models.ManyToManyField(
        'post.Post',
        verbose_name='좋아요 누른 포스트 목록'
    )
    # 내가 팔로우하고 있는 유저 목록
    # 내가 A를 follow 한다
    #   나는 A의 follower이며
    #   A는 나의 following_user이다

    # 나를 follow하고 있는 사람 목록은
    #   followers
    # 내가 follow하고 있는 사람 목록은
    #   following_users
    following_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='followers'
    )
    objects = UserManager()

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = f'{verbose_name} 목록'

    def follow_toggle(self, user):
        if not isinstance(user, User):
            raise ValueError('"user" argument must be User instance!')

        relation, relation_created = self.following_user.get_or_create(to_user=user)
        if relation_created:
            return True
        relation.delete()
        return False

        # if user in self.following_users.all():
        #     Relation.objects.filter(
        #         from_user=self,
        #         to_user=user,
        #     ).delete()
        # else:
        #     self.following_user_relations.create(to_user=user)
        #     Relation.objects.create(
        #         from_user=self,
        #         to_user=user,
        #     )


class Relation(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following_user_relations'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower_relations'
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Relation ('f'from: {self.from_user.username}, 'f'to: {self.to_user.username})'
