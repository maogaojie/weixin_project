from rest_framework import serializers




from orders.models import MyCoupon, Order, Coupon

# 优惠
class CouponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


# 我的优惠卷

class MyCouponSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    coupon = CouponModelSerializer()


    class Meta:
        model = MyCoupon
        fields = '__all__'

# 订单序反列化
class OrderSerializer(serializers.Serializer):
    order_number = serializers.CharField(max_length=255)  # 订单编号
    course_id = serializers.IntegerField()  # 课程
    user_id = serializers.IntegerField()  # 用户
    code = serializers.CharField()  # 到店验证码
    coach = serializers.CharField()  # 教练
    is_coupon = serializers.BooleanField(default=False)  # 是否使用优惠卷
    mycoupon_id = serializers.IntegerField(allow_null=True)  # 优惠卷
    total_money = serializers.DecimalField(max_digits=7,decimal_places=2)
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order
