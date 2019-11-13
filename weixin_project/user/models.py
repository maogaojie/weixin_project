from django.db import models
from course.models import Store, Tag, Course


# Create your models here.

class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        如果你想把某些公共信息添加到很多 model 中，抽象基类就显得非常有用。
        你编写完基类之后，在 Meta 内嵌类中设置 abstract=True ，
        该类就不能创建任何数据表。然而如果将它做为其他 model 的基类，那么该类的字段就会被添加到子类中。
        抽象基类和子类如果含有同名字段，就会导致错误(Django 将抛出异常)。
        """
        abstract = True  # 不用创建表可以省区重复写的代码直接继承就可以使用


# 用户
class User(Base, models.Model):
    openid = models.CharField(max_length=128, unique=True)  # 微信返回用户唯一标识码
    username = models.CharField(max_length=128)
    invitation_code = models.CharField(max_length=128)  # 邀请码
    invitation_num = models.IntegerField(default=0)  # 发出邀请数量
    succeed_invitation = models.IntegerField(default=0)  # 成功邀请的人数
    age = models.IntegerField()
    gender = models.IntegerField()  # 1男 2女

    class Meta:
        db_table = 'user'


# 用户信息
class UserInfor(Base, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    is_gender = {
        (1, '男'),
        (2, '女')
    }
    gender = models.IntegerField(choices=is_gender)  # 性别
    birthday = models.DateField()  # 生日
    tall = models.FloatField()  # 身高
    weight = models.FloatField()  # 体重
    BMI = models.FloatField()
    aim_weight = models.FloatField()  # 目标体重
    hopes = {
        (1, '减脂塑性'),
        (2, '增肌塑形'),
        (3, '体态改善')
    }
    hope = models.IntegerField(choices=hopes)  # 希望改变
    tag = models.ManyToManyField(Tag)  # 标签
    days = {
        (1, '2天'),
        (2, '3天'),
        (3, '4天'),
        (4, '5天'),
    }
    day = models.IntegerField(choices=days)  # 每周训练几天
    times = {
        (1, '45分钟'),
        (2, '60分钟'),
        (3, '90分钟'),
        (4, '105分钟'),
    }
    how_long = models.IntegerField(choices=times)  # 每天训练多长时间

    class Meta:
        db_table = 'userinfor'
        verbose_name_plural = '用户信息计划表'

    def __str__(self):
        return self.username

# 用户信息
class UserInformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    height = models.CharField(max_length=5,null=True,blank=True,default='')
    weight = models.CharField(max_length=5,null=True,blank=True,default='')
    phone = models.CharField(max_length=11,null=True,blank=True,default='')

    class Meta:
        db_table = 'userinformation'
