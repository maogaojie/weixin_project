from rest_framework import serializers

from orders.models import MyCoupon, Order


# 我的优惠卷
class MyCouponSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    coupon = serializers.CharField(source='coupon.name')
    status = serializers.CharField(source='is_status')

    class Meta:
        model = MyCoupon
        fields = '__all__'

# 订单序反列化
class OrderSerializer(serializers.Serializer):
    order_number = serializers.CharField(max_length=255)  # 订单编号
    money = serializers.CharField(max_length=15)  # 金额
    course_id = serializers.IntegerField()  # 课程
    user_id = serializers.IntegerField()  # 用户
    code = serializers.CharField()  # 到店验证码
    coach_id = serializers.IntegerField()  # 教练
    is_coupon = serializers.BooleanField(default=False)  # 是否使用优惠卷
    mycoupon_id = serializers.IntegerField(allow_null=True)  # 优惠卷

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order
