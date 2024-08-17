from rest_framework import serializers


class JoatssRequestSerializer(serializers.Serializer):
    text = serializers.CharField(allow_blank=True)


class JoatssResponseSerializer(serializers.Serializer):
    answer = serializers.CharField()
