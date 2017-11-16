"""
class SMSSerializer:
    receiver에 휴대전화 형식의 데이터가 왔는지 validate
    message에 90자 이하의 문자열이 왔는지 validate

    is_valid() 검사 후
        serializer.data에 있는 내용을 이용해서 send 처리
"""
from rest_framework import serializers


def validate_receiver(value):
    if not len(str(value)) == 11:
        raise serializers.ValidationError('ex) 01000000000')


def validate_message(value):
    if not len(value) <= 90:
        raise serializers.ValidationError('메시지는 90자로 제한합니다.')


class SMSSerializer(serializers.Serializer):
    receiver = serializers.IntegerField(validators=[validate_receiver])
    message = serializers.CharField(validators=[validate_message])
