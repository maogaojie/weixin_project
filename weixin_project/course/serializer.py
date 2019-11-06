from course import models
from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    oname = serializers.CharField()
    money_one = serializers.DecimalField(max_digits=7, decimal_places=2)  # 花费的钱
    money_two = serializers.IntegerField()  # 花费的课包 1个课包，2两个课包。。。
    pay_type = serializers.BooleanField()  # 支付方式
    information = serializers.CharField()  # 介绍签名
    coach_id = serializers.IntegerField()  # 教练
    address_id = serializers.IntegerField()  # 地址
    store_name = serializers.CharField(max_length=128)  # 店名
    coursetime_id = serializers.IntegerField()  # 课程花费的时间
    coursetype_id = serializers.IntegerField()  # 课程的类型
    coursestatus = serializers.IntegerField()  # 课程状态
    image = serializers.ImageField()

    def create(self, validated_data):
        course = models.Course.objects.create(**validated_data)
        return course



