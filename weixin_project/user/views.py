from django.shortcuts import render

# Create your views here.
import uuid

from rest_framework.response import Response
from user import models
from user import serializer
from rest_framework.views import APIView
from utils.openid import get_openid


class GetCode(APIView):
    """
    获取code
    存储唯一openid
    """

    def post(self, request):
        mes = {}
        data = request.data.copy()
        code = data['code']
        print(code)
        openid = get_openid(code)
        user = models.User.objects.filter(openid=openid).first()
        if user:
            mes['code'] = 200
            mes['message'] = '登录成功'
            mes['user_id'] = user.id
        else:
            data['openid'] = openid
            data['invitation_code'] = uuid.uuid1()
            print(data)
            user = serializer.UserSerializer(data=data)
            if user.is_valid():
                user.save()
                user = models.User.objects.filter(openid=openid).first()
                mes['code'] = 0
                mes['message'] = '授权成功'
                mes['user_id'] = user.id
            else:
                mes['code'] = 1
                mes['message'] = '授权失败'
        return Response(mes)


class UserInforAPIView(APIView):
    """
    用户详情
    计划
    """
    def post(self, request):
        mes = {}
        data = request.data
        user = serializer.UserInforSerializer(data=data)
        if user.is_valid():
            user.save()
            mes['code'] = 200
        else:
            mes['code'] = 1001
        return Response(mes)


class SubscribeAPIView(APIView):
    """
    预约
    """
    def post(self, request):
        mes = {}
        data = request.data
        if models.YuYUE.objects.filter(course_id=data['course_id'],user_id=data['user_id']).first():
            mes['code'] = 200
            mes['message'] = '已经预约'
        subscribe = serializer.SubscribeSerializer(data=data)
        if subscribe.is_valid:
            subscribe.save()
            mes['code'] = 200
        else:
            mes['code'] = 1001
        return Response(mes)


class MySubscribe(APIView):
    """
    我的预约
    """
    def get(self, request):
        mes = {}
        yuyue_list = models.YuYUE.objects.filter(user_id=user_id).all()

        return Response(mes)
