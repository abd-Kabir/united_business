import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger()


class PaymeEndpointURL(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        logger.debug(f"Data: {request.data}; Params: {request.query_params}")
        return Response({
            "detail": "Successfully Done",
            "status": status.HTTP_200_OK
        })
