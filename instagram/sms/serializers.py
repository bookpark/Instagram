"""
class SMSSerializer:
    receiver에 휴대전화 형식의 데이터가 왔는지 validate
    message에 90자 이하의 문자열이 왔는지 validate

    is_valid() 검사 후
        serializer.data에 있는 내용을 이용해서 send 처리
"""
from rest_framework import serializers

from sms.validators import phone_number, sms_length


class SMSSerializer(serializers.Serializer):
    receiver = serializers.CharField(
        validators=[phone_number]
    )
    message = serializers.CharField(
        validators=[sms_length]
    )

    def validate_receiver(self, value):
        return value.replace('-', '')
