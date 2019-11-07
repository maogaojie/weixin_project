from django.db import models
from user.models import Base, Coach




# 精准地址
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)  # 加后缀名 省市区
    pid = models.IntegerField()
    sname = models.CharField(max_length=128)  # 不加后缀
    level = models.IntegerField()  # 等级
    citycode = models.CharField(max_length=128, null=True, blank=True)  # 城市区号
    yzcode = models.CharField(max_length=128, null=True, blank=True)  # 城市邮编
    mername = models.CharField(max_length=128)  # 所在地区联名 (中国,北京,北京市)
    Lng = models.FloatField()  # 经度
    Lat = models.FloatField()  # 纬度
    pinyin = models.CharField(max_length=128)

    class Meta:
        db_table = 'region'


# 排课表
class CourseTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    spend_time = models.IntegerField()  # 花费时间

    class Meta:
        db_table = 'coursetime'


class CourseType(models.Model):
    name = models.CharField(max_length=128)  # 课程分类名称

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
    pay_type = models.BooleanField(choices=pay)  # 支付方式
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)  # 教练
    city = models.ForeignKey(Region, on_delete=models.CASCADE)  # 地址
    store_name = models.CharField(max_length=128)  # 店名
    coursetime = models.ForeignKey(CourseTime, on_delete=models.CASCADE)  # 课程花费的时间
    coursetype = models.ForeignKey(CourseType, on_delete=models.CASCADE)  # 课程的类型
    status = {
        (1, '人数已满'),
        (2, '未满'),
        (3, '已结束'),
        (4, '已预约'),
    }
    coursestatus = models.IntegerField(choices=status)  # 课程状态
    image = models.ImageField(upload_to='course')

    class Meta:
        db_table = 'course'


class CourseDetail(models.Model):
    course = models.ForeignKey(Course, on_delete=True)
    course_ntroduction = models.CharField(max_length=255) # 课程介绍
    training_effect = models.CharField(max_length=255) # 训练效果
    crowd = models.CharField(max_length=255) # 适合人群
    FQA = models.CharField(max_length=255) # FQA
    notice = models.CharField(max_length=255) # 注意事项

    class Meta:
        db_table = 'coursedetail'
