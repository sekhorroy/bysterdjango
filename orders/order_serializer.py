from rest_framework import serializers
from .models import MtOrder

class MtOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtOrder
        fields = ['order_id','merchant_id','client_id','total_w_tax','status','delivery_charge','date_created']
