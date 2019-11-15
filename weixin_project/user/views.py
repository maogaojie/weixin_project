from django.shortcuts import render

# Create your views here.
import uuid
import datetime
import redis
from rest_framework.response import Response
from user import models
from user import serializer
from rest_framework.views import APIView
from utils.openid import get_openid
from utils.aes import AesEncryption
from orders.models import MyCoupon
from weixin_project.settings import key

pool = redis.ConnectionPool(host='120.27.247.213', port=6379, password='foobared')
r = redis.Redis(connection_pool=pool)

def create_token(id):
    aes = AesEncryption(key)
    token = aes.encrypt(str(id))  # 调用加密函数
    return token



def check_token(token,id):
    aes = AesEncryption(key)
    check = aes.decrypt(token)  # 调用解密函数
    data = r.get('toekn'+str(id))

    return data





def add_coupon(id):
    """第一次登录送30元优惠卷"""
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=60)
    n_days = now + delta
    n_days = n_days.strftime('%Y-%m-%d %H:%M:%S')
    MyCoupon.objects.create(user_id=id,name='新人优惠30元',coupon_id=1,number=1,expiration_time=n_days,status=1)



class GetCode(APIView):
    """
    获取code
    存储唯一openid
    """

    def post(self, request):

        mes = {}
        data = request.data.copy()
        code = data['code']
        openid = get_openid(code)
        user = models.User.objects.filter(openid=openid).first()
        if user:
            mes['code'] = 200
            mes['message'] = '登录成功'
            mes['user_id'] = user.id
            token = create_token(user.id)
            mes['token'] = token
            # r.set('token'+str(user.id), token ,60)

        else:
            data['openid'] = openid
            data['invitation_code'] = str(uuid.uuid1())
            data['age'] = 0
            user = serializer.UserSerializer(data=data)
            if user.is_valid():
                user.save()
                user = models.User.objects.filter(openid=openid).first()
                add_coupon(user.id)
                mes['code'] = 0
                mes['message'] = '授权成功'
                mes['user_id'] = user.id
                token = create_token(user.id)
                mes['token'] = token
                r.set('token'+str(user.id), token ,60)
            else:
                mes['code'] = 1
                mes['message'] = '授权失败'
        return Response(mes)


class UserInforAPIView(APIView):
    """
    用户详情
    """
    def get(self,request):
        mes = {}
        try:
            user_id = request.GET.get('user_id')
        except Exception as e:
            mes['code'] = 1001
            return Response(mes)
        one_user = models.UserInformation.objects.filter(user_id=user_id).first()
        one_user = serializer.UserInformationModelSerializer(one_user,many=False)
        if one_user:
            mes['code'] = 200
            mes['userinfor'] = one_user.data
            return Response(mes)


    def post(self, request):
        mes = {}
        data = request.data.copy()
        print(data)
        user_id = data['user_id']
        one_user = models.UserInformation.objects.filter(user_id=user_id).first()
        if not one_user:
            user = serializer.UserInformationSerializer(data=data)
        else:
            user = serializer.UserInformationSerializer(instance=one_user,data=data)
        if user.is_valid():
            user.save()
            mes['code'] = 200
            userinfor = models.UserInformation.objects.filter(user_id=user_id).first()
            mes['height'] = userinfor.height
            mes['weight'] = userinfor.weight
            mes['phone'] = userinfor.phone
        else:
            print(user.errors)
            mes['code'] = 1001
        return Response(mes)
