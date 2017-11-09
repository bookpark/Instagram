import io
import os
from random import randint

from django.conf import settings
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

    @staticmethod
    def create_user(username='dummmy'):
        return User.objects.create_user(username=username, age=0)

    @staticmethod
    def create_post(author=None):
        return Post.objects.create(author=author, photo=File(io.BytesIO))

    def test_post_list_url_name_reverse(self):
        url = reverse(self.URL_API_POST_LIST_NAME)
        self.assertEqual(url, self.URL_API_POST_LIST)

    def test_post_list_url_resolve_view_class(self):
        """
        post.apis.PostList 뷰에 대해
        URL reverse, resolve, 사용하고 있는 view 함수가 같은지 확인
        :return:
        """
        # /api/posts/에 매칭디는 ResolverMatch 객체를 가져옴
        resolver_match = resolve(self.URL_API_POST_LIST)
        # ResolverMatch의 url_name이 'api-post'(self.URL_API_POST_LIST_NAME)인지 확인
        self.assertEqual(resolver_match.url_name, self.URL_API_POST_LIST_NAME)
        # ResolverMatch의 func이 PostList(self.VIEW_CLASS)인지 확인
        self.assertEqual(resolver_match.func.view_class, self.VIEW_CLASS)

    def test_get_post_list(self):
        """
        PostList의 GET 요청 (Post 목록)에 대한 테스트
        임의의 갯수만큼 Post를 생성하고 해당 갯수만큼 Response가 돌아오는지 확
        :return:
        """
        user = self.create_user()
        # 0 이상 20 이하의 임의의 숫자 지정
        num = randint(0, 20)
        # num 갯수만큼 Post 생성
        for i in range(num):
            self.create_post(author=user)
        url = reverse(self.URL_API_POST_LIST_NAME)
        # post_list에 GET요청
        response = self.client.get(url)
        # status_code가 200인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response로 돌아온 JSON 리스트의 길이가 num과 같은지 확인
        self.assertEqual(len(response.data), num)

        # response로 돌아온 객체들이 각각 pk, author, photo, created_at
        for i in range(num):
            cur_post_data = response.data[i]
            self.assertIn('pk', cur_post_data)
            self.assertIn('author', cur_post_data)
            self.assertIn('photo', cur_post_data)
            self.assertIn('created_at', cur_post_data)

    def test_get_post_list_exclude_author_is_none(self):
        """
        author가 None인 post가 PostList get 요청에서 제외되는지 테스트
        :return:
        """
        user = self.create_user()
        num_author_none_posts = randint(0, 10)
        num_posts = randint(11, 20)
        for i in range(num_author_none_posts):
            self.create_post()
        for i in range(num_posts):
            self.create_post(author=user)

        response = self.client.get(self.URL_API_POST_LIST)
        # author가 없는 Post 갯수는 response에 포함되지 않는지 확인
        self.assertEqual(len(response.data), num_posts)

    def test_create_post(self):
        """
        Post Create이 되는지 확인
        :return:
        """
        # 테스트용 유저 생성
        user = self.create_user()
        # 해당 유저를 현재 client에 강제로 인증
        self.client.force_authenticate(user=user)
        # 테스트용 이미지 파일의 경로
        path = os.path.join(settings.STATIC_DIR, 'test', 'joy8.jpg')

        # path에 해당하는 파일을 post요청에 'photo'키의 값으로 전달
        with open(path, 'rb') as photo:
            response = self.client.post('/api/posts/', {
                'photo': photo,
            })
        # response 코드가 201인지 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 1개의 포스트가 생성되었는지 확인
        self.assertEqual(Post.objects.count(), 1)

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
