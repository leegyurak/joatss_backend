from rest_framework import serializers


class JoatssSerializer(serializers.Serializer):
    text = serializers.CharField()
