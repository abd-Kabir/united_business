from rest_framework import serializers

from apps.trade.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['TNVED',
                  'product', ]
