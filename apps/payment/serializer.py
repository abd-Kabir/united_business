from rest_framework import serializers

from apps.payment.methods import METHODS


class PaymeMerchantAPISerializer(serializers.Serializer):

    id = serializers.IntegerField()
    method = serializers.ChoiceField(choices=METHODS)
    params = serializers.JSONField()
