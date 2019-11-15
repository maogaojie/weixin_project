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


# 用户详情反序列化
class UserInformationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    height = serializers.CharField(allow_null=True)
    weight = serializers.CharField(allow_null=True)
    phone = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        user_infor = models.UserInformation.objects.create(**validated_data)
        return user_infor
    def update(self, instance, validated_data):
        print(instance)
        instance.user_id = validated_data['user_id']
        instance.height = validated_data['height'] if validated_data.get('height')!='0' else instance.height
        instance.weight = validated_data['weight'] if validated_data.get('weight')!='0' else instance.weight
        instance.phone = validated_data['phone'] if validated_data.get('phone')!='0' else instance.phone
        instance.save()

        return instance


class UserInformationModelSerializer(serializers.ModelSerializer):

    """ 用户详情序列化 """
    class Meta:
        model = models.UserInformation
        fields = '__all__'
