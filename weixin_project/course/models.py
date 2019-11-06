from django.db import models
from user.models import *


# 地址
class City(models.Model):
    pid = models.IntegerField()  # 上一级id
    cityname = models.CharField(max_length=128)
    type = models.IntegerField()  # 级别

    class Meta:
        db_table = 'city'

# 排课表
class CourseTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    send_time = models.IntegerField()  # 花费时间

    class Meta:
        db_table = 'coursetime'


class CourseType(models.Model):
    name = models.CharField(max_length=128) # 课程分类名称

    class Meta:
        db_table = 'courseType'


# 课程表
class Course(Base, models.Model):
    name = models.CharField(max_length=128)
    money_one = models.DecimalField(max_digits=7, decimal_places=2)  # 花费的钱
    money_two = models.IntegerField()  # 花费的课包 1个课包，2两个课包。。。
    pay = {
        (1, '课包支付'),
        (2, '现金支付')
    }
    pay_type = models.BooleanField()  # 支付方式
    information = models.CharField(max_length=255)  # 介绍签名
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    address = models.ForeignKey(City, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=128) # 店名
    coursetime = models.ForeignKey(CourseTime, on_delete=models.CASCADE)
    coursetype = models.ForeignKey(CourseType,on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        db_table = 'course'


