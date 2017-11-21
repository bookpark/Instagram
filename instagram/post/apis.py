from rest_framework import generics, permissions
from rest_framework.response import Response

from member.serializers import UserSerializer
from utils.pagination import PostPagination
from utils.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        # 인증 된 사용자만 리스트를 볼 수 있음
        permissions.IsAuthenticated,
    )
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
    )


class PostLikeToggle(generics.GenericAPIView):
    queryset = Post.objects.all()
    # url 패턴에서 특정 Post instance를 가져오기 위한 그룹명
    lookup_url_kwarg = 'post_pk'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        # 이미 유저의 like_posts 목록에 현재 post(instance)가 존재할 경우
        if instance in user.like_posts.all():
            user.like_posts.remove(instance)
            like_status = False
        else:
            user.like_posts.add(instance)
            like_status = True
        data = {
            'user': UserSerializer(user).data,
            'post': PostSerializer(instance).data,
            'result': like_status,
        }
        return Response(data)
