from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SMSSerializer


class SendSMS(APIView):
    def post(self, request):
        serializer = SMSSerializer(request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # api_key = "NCSGLMHSQ2FTVZUA"
        # api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"
        #
        # receiver = serializer_receiver.data
        # message = serializer_message.data
        #
        # params = dict()
        # params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
        # params['to'] = receiver  # Recipients Number '01000000000,01000000001'
        # params['from'] = '01029953874'  # Sender number
        # params['text'] = message  # Message
        #
        # cool = Message(api_key, api_secret)
        # try:
        #     response = cool.send(params)
        #     print("Success Count : %s" % response['success_count'])
        #     print("Error Count : %s" % response['error_count'])
        #     print("Group ID : %s" % response['group_id'])
        #
        #     if "error_list" in response:
        #         print("Error List : %s" % response['error_list'])
        #
        # except CoolsmsException as e:
        #     print("Error Code : %s" % e.code)
        #     print("Error Message : %s" % e.msg)
        #
        # if serializer_receiver.is_valid() and serializer_message.is_valid():
        #     serializer_receiver.save() and serializer_message.save()
        #
        # return Response(status=status.HTTP_200_OK)
