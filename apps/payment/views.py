import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.payment.serializer import PaymeMerchantAPISerializer
from apps.tools.utils.paycom import paycom_method

logger = logging.getLogger()


class PaymeEndpointURL(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        logger.debug(f"Data: {request.data}; Params: {request.query_params}")

        serializer = PaymeMerchantAPISerializer(data=request.data)
        method = serializer.data['method']
        params = serializer.data['params']

        response = paycom_method(method, params)

        return Response(response)
