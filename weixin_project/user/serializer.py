from user import models
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    openid = serializers.CharField()  # 微信返回用户唯一标识码
    username = serializers.CharField(max_length=128)
    invitation_code = serializers.CharField(max_length=128)  # 邀请码
    invitation_num = serializers.IntegerField(default=0)  # 发出邀请数量
    succeed_invitation = serializers.IntegerField(default=0)  # 成功邀请的人数
    age = serializers.IntegerField()
    gender = serializers.IntegerField()  # 1男 2女
    image = serializers.CharField()

    def create(self, validated_data):
        user = models.User.objects.create(**validated_data)
        return user


# 用户详情反序列化
class UserInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfor
        fields = '__all__'

    def create(self, validated_data):
        tag = validated_data.pop('tag')

        user_infor = models.UserInfor.objects.create(**validated_data)
        for t in tag:
            t = models.Tag.objects.filter(id=t.id).first()
            user_infor.tag.add(tag)
            user_infor.save()
        return user_infor


class SubscribeSerializer(serializers.Serializer):
    """预约表反序列化"""
    course_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    def create(self, validated_data):
        plan = models.YuYUE.objects.create(**validated_data)
        return plan
