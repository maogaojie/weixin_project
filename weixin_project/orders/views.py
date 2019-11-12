import random
import uuid

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from orders import models
from orders.serializer import MyCouponSerializer
from orders import serializer


def random_str():
    num_ = [str(i) for i in range(9)]
    a_ = [chr(i) for i in range(97, 123)]
    A_ = [chr(x) for x in range(65, 91)]
    return ''.join(random.sample(num_ + a_ + A_, 6))


class MyCouponAPIView(APIView):
    def get(self, request):
        mes = {}

        coupon_list = models.MyCoupon.objects.filter(user_id=request.GET.get('user_id')).all()
        coupon_list = MyCouponSerializer(coupon_list, many=True)
        mes['code'] = 200
        mes['coupon_list'] = coupon_list.data
        return Response(mes)


class ReserveAPIView(APIView):
    """
    生成订单
    """
    def post(self, request):
        mes = {}
        data = request.data.copy()
        data['order_number'] = str(uuid.uuid1())
        data['code'] = random_str()
        order = serializer.OrderSerializer(data=data)
        if order.is_valid():
            order.save()
            mes['code'] = 200
        else:
            mes['code'] = 1001
        return Response(mes)
