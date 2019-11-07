from django.shortcuts import render

# Create your views here.
import uuid
import json
import urllib.request
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


# 基于百度地图API下的经纬度信息来解析地理位置信息
# json序列化解析数据(lat:纬度，lng:经度)
class Address(APIView):
    def get(self, request):
        lat = request.GET.get('lat')  # 纬度
        lng = request.GET.get('lng') # 经度
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=NQDOSRjhU1cWFGlKPXLTuX8kSeNGYdfR&output=json&coordtype=wgs84ll&location=' + lat + ',' + lng
        req = urllib.request.urlopen(url)  # json格式的返回数据
        print(req)
        res = req.read().decode("utf-8")  # 将其他编码的字符串解码成unicode
        str = json.loads(res)
        print(str)
        dictjson = {}  # 声明一个字典
        # get()获取json里面的数据
        jsonResult = str.get('result')
        address = jsonResult.get('addressComponent')
        # 国家
        country = address.get('country')
        # 国家编号（0：中国）
        country_code = address.get('country_code')
        # 省
        province = address.get('province')
        # 城市
        city = address.get('city')
        # 城市等级
        city_level = address.get('city_level')
        # 县级
        district = address.get('district')
        # 把获取到的值，添加到字典里（添加）
        dictjson['country'] = country
        dictjson['country_code'] = country_code
        dictjson['province'] = province
        dictjson['city'] = city
        dictjson['city_level'] = city_level
        dictjson['district'] = district
        return Response(dictjson)

