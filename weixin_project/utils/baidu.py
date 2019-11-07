import json
import urllib.request

from course import models, serializer


# 基于百度地图API下的经纬度信息来解析地理位置信息
# json序列化解析数据(lat:纬度，lng:经度)
def get_address(lat, lng):
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=NQDOSRjhU1cWFGlKPXLTuX8kSeNGYdfR&output=json&coordtype=wgs84ll&location=' + lat + ',' + lng
    req = urllib.request.urlopen(url)  # json格式的返回数据
    res = req.read().decode("utf-8")  # 将其他编码的字符串解码成unicode
    str = json.loads(res)
    mes = {}  # 声明一个字典
    # get()获取json里面的数据
    jsonResult = str.get('result')
    address = jsonResult.get('addressComponent')
    # 把获取到的值，添加到字典里（添加）
    mes['country'] = address.get('country')  # 国家
    mes['country_code'] = address.get('country_code')  # 国家编号（0：中国）
    mes['province'] = address.get('province')  # 省
    mes['city'] = city = address.get('city')  # 城市
    mes['city_level'] = address.get('city_level')  # 城市等级
    mes['district'] = address.get('district')  # 县级
    store = models.Store.objects.filter(city__name=address.get('district')).all()
    print(store)
    store = serializer.StoreModelSerializer(store, many=True)
    mes['store'] = store.data
    return mes
