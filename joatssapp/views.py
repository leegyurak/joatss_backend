import re

from rest_framework import status
from rest_framework.exceptions import ValidationError as DrfValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from joatssapp.dtos import JoatssDto
from joatssapp.exceptions import FailedToGetJoatssAnswerError
from joatssapp.serializers import JoatssResponseSerializer, JoatssRequestSerializer
from joatssapp.services import JoatssService


class JoatssView(APIView):    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        request_serializer: JoatssRequestSerializer = JoatssRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        try:
            dto: JoatssDto = JoatssService().get_joatss_answer(
                ip=self.get_client_ip(request),
                text=request_serializer.validated_data['text'],
            )
        except FailedToGetJoatssAnswerError as error:
            raise DrfValidationError(detail=error.message) from error
        response_serializer: JoatssResponseSerializer = JoatssResponseSerializer(dto)
        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK,
        )
