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




