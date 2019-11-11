from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from orders import models
from orders.serializer import MyCouponSerializer


class MyCouponAPIView(APIView):
    def get(self, request):
        mes = {}
        coupon_list = models.MyCoupon.objects.filter(user_id=request.GET.get('user_id')).all()
        coupon_list = MyCouponSerializer(coupon_list, many=True)
        mes['code'] = 200
        mes['coupon_list'] = coupon_list.data
        return Response(mes)

