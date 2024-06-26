from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    field_name = serializers.ListField(child=serializers.CharField(max_length=256))


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=256)
