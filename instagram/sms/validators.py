from rest_framework import serializers


def phone_number(value):
    value = value.replace('-', '')
    # if len(value) not in (10, 11):
    if len(value) != 10 or len(value) != 11:
        raise serializers.ValidationError('번호가 유효하지 않습니다')
    if not value.startswith('0'):
        raise serializers.ValidationError('번호가 유효하지 않습니다')


def sms_length(value):
    encoded_str = value.encode('cp949')
    if len(encoded_str) > 90:
        raise serializers.ValidationError(
            f'메시지는 90byte로 제한합니다. (요청길이: {len(encoded_str)})'
        )
