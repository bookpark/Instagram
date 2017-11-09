import io
from random import randint

from django.contrib.auth import get_user_model
from django.core.files import File
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from post.apis import PostList
from post.models import Post

User = get_user_model()


class PostListViewTest(APILiveServerTestCase):
    URL_API_POST_LIST_NAME = 'api-post'
    URL_API_POST_LIST = '/api/posts/'
    VIEW_CLASS = PostList

    def test_post_list_url_name_reverse(self):
        url = reverse(self.URL_API_POST_LIST_NAME)
        self.assertEqual(url, self.URL_API_POST_LIST)

    def test_post_list_url_resolve_view_class(self):
        # /api/posts/에 매칭디는 ResolverMatch 객체를 가져옴
        resolver_match = resolve(self.URL_API_POST_LIST)
        # ResolverMatch의 url_name이 'api-post'(self.URL_API_POST_LIST_NAME)인지 확인
        self.assertEqual(resolver_match.url_name, self.URL_API_POST_LIST_NAME)
        # ResolverMatch의 func이 PostList(self.VIEW_CLASS)인지 확인
        self.assertEqual(resolver_match.func.view_class, self.VIEW_CLASS)

    def test_get_post_list(self):
        user = User.objects.create(username='dummy', age=0)
        # 0 이상 20 이하의 임의의 숫자 지정
        num = randint(0, 20)
        # num 갯수만큼 Post 생성
        for i in range(num):
            Post.objects.create(
                author=user,
                photo=File(io.BytesIO())
            )
        url = reverse(self.URL_API_POST_LIST_NAME)
        # post_list에 GET요청
        response = self.client.get(url)
        # status_code가 200인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response로 돌아온 JSON 리스트의 길이가 num과 같은지 확인
        self.assertEqual(len(response.data), num)

# # PostList
# # Request 객체를 생성 ('api/posts/')
# url = reverse('api-post')
# factory = APIRequestFactory()
# request = factory.get('api/posts/')
#
# # PostList.as_view()로 생성한 뷰 함수를 'view' 변수에 할당
# view = PostList.as_view()
# # view 함수에 request를 전달
# response = view(request)
#
# # 결과는 JSON 데이터
# pprint(response.data)
