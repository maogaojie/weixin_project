from django.shortcuts import render

# Create your views here.
import uuid
import requests, json
from rest_framework.response import Response

from user.serializer import *
from rest_framework.views import APIView


def get_openid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx3e01b136e25ff2b2&secret=7fd7e71462aa0f11fe254b36371efb26&js_code=%s&grant_type=authorization_code' % code
    res = requests.get(url)
    print(res)
    return json.loads(res.text)['openid']


class GetCode(APIView):
    def post(self, request):
        mes = {}
        data = request.data.copy()
        code = data['code']
        openid = get_openid(code)
        data['openid'] = openid
        data['invitation_code'] = uuid.uuid1()
        print(data)
        user = UserSerializer(data=data)
        if user.is_valid():
            user.save()
            mes['code'] = 0
            mes['message'] = '授权成功'
        else:
            mes['code'] = 1
            mes['message'] = '授权失败'
        return Response(mes)
