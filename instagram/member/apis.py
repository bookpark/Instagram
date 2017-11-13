from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, SignupSerializer

User = get_user_model()


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        # 전달받은 username, password 값으로
        # authenticate 실행
        user = authenticate(
            username=username,
            password=password,
        )
        # user가 존재할 경우 (authenticate 성공)
        if user:
            token, token_created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user': UserSerializer(user).data,
            }
            return Response(data, status=status.HTTP_200_OK)

        # 실패한 경우
        else:
            data = {
                'username': username,
                'password': password,
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class Signup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
