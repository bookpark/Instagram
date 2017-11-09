from django.urls import reverse, resolve
from rest_framework.test import APILiveServerTestCase


class PostListViewTest(APILiveServerTestCase):
    URL_API_POST_LIST_NAME = 'api-post'
    URL_API_POST_LIST = '/api/posts/'

    def test_post_list_url_name_reverse(self):
        url = reverse(self.URL_API_POST_LIST_NAME)
        self.assertEqual(url, self.URL_API_POST_LIST)

    def test_post_list_url_resolve(self):
        resolver_match = resolve(self.URL_API_POST_LIST)
        self.assertEqual(resolver_match.url_name, self.URL_API_POST_LIST_NAME)


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
