from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sms.coolsms import send_sms
from .serializers import SMSSerializer


class SendSMS(APIView):
    def post(self, request):
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            # 직접 serializer에서 data꺼내와서 사용
            # receiver = serializer.data['receiver']
            # message = serializer.data['message']
            # result = send_sms(receiver=receiver, message=message)

            # dict의 key/value를 호출 인수/값으로 사용하는 **표현식 사용
            result = send_sms(**serializer.data)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
