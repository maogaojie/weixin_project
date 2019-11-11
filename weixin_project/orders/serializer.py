from rest_framework import serializers

from orders.models import MyCoupon


class MyCouponSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name')
    coupon = serializers.CharField(source='coupon.name')
    status = serializers.IntegerField(source='is_status')

    class Meta:
        module = MyCoupon
        fields = '__all__'
