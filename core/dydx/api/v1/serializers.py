from rest_framework.serializers import ModelSerializer
from ...models import Positions,HistoryTransfers,HistoryTrades,HistoryFunding

class PositionSerializer(ModelSerializer):

    class Meta:
        model = Positions
        fields = [
            "id",
            "user",
            "market",
            "long",
            "size",
            "leverage",
            "realized_PL",
            "average_open",
            "margin_used",
            "created_date",
            "updated_date",
        ]


    def to_representation(self, instance):
        rep = super().to_representation(instance)
    
        return rep
    
class HistoryTradesSerializer(ModelSerializer):

    class Meta:
        model = HistoryTrades
        fields = [
            "id",
            "user",
            "time",
            "market",
            "long",
            "amount",
            "price",
            "total",
            "fee",
            "tradetype",
            "liquidity",
            "created_date",
            "updated_date",
            'creation_time'
        ]
    
class HistoryTransferSerializer(ModelSerializer):

    class Meta:
        model = HistoryTransfers
        fields = [
            "id",
            "user",
            "time",
            "action",
            "status",
            "amount",
            "transaction",
            "transaction_link",
            "fee",
            "created_date",
            "updated_date",
            'creation_time'
        ]


    def to_representation(self, instance):
        rep = super().to_representation(instance)
    
        return rep
    
class HistoryFundingSerializer(ModelSerializer):

    class Meta:
        model = HistoryFunding
        fields = [
            "id",
            "user",
            "time",
            "market",
            "funding_rate",
            "long",
            "payment",
            "ppsition",
            "position_asset",
            "created_date",
            "updated_date",
            'creation_time'
        ]


    def to_representation(self, instance):
        rep = super().to_representation(instance)
    
        return rep
