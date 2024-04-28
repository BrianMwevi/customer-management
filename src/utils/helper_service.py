
from .serializers import ErrorSerializer, MessageSerializer


def swagger_response_builder(serializer=MessageSerializer, code=200):
    return {code: serializer, 400: ErrorSerializer, 401: ErrorSerializer}

