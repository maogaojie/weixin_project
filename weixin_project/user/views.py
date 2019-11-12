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
        if models.User.objects.filter(openid=openid).first():
            mes['code'] = 200
            mes['message'] = '登录成功'
        else:
            data['openid'] = openid
            data['invitation_code'] = uuid.uuid1()
            print(data)
            user = serializer.UserSerializer(data=data)
            if user.is_valid():
                user.save()
                mes['code'] = 0
                mes['message'] = '授权成功'
            else:
                mes['code'] = 1
                mes['message'] = '授权失败'
        return Response(mes)


class PlanAPIView(APIView):
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
