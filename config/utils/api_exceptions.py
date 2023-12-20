from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.utils.translation import gettext_lazy as _

import logging

logger = logging.getLogger()


class APIValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message_detail = 'Service temporarily unavailable, try again later.'
    message_code = 'error'

    def __init__(self, message=None, code=None, status_code=status_code):
        self.status_code = status_code
        super().__init__(message, code)


def uni_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    if response:
        if response.status_code == 401:
            response = Response({'message': _('No active account found with the given credentials'),
                                 'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
            return response
        return response
