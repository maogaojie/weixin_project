from django.db import models


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
class User(Base,models.Model):
    openid = models.CharField(max_length=128,unique=True)  # 微信返回用户唯一标识码
    username = models.CharField(max_length=128)
    invitation_code = models.CharField(max_length=128)  # 邀请码
    invitation_num = models.IntegerField(default=0)  # 发出邀请数量
    succeed_invitation = models.IntegerField(default=0)  # 成功邀请的人数
    age = models.IntegerField()
    gender = models.IntegerField()  # 1男 2女

    class Meta:
        db_table = 'user'


# 用户信息
class UserInfor(Base,models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    is_gender = {
        (1, '男'),
        (2, '女')
    }
    gender = models.BooleanField(choices=is_gender)
    birthday = models.DateField()
    tall = models.FloatField()  # 身高
    weight = models.FloatField()  # 体重
    BMI = models.FloatField()

    class Meta:
        db_table = 'userinfor'


# 教练
class Coach(Base,models.Model):
    coach_name = models.CharField(max_length=128)
    openid = models.CharField(max_length=128,unique=True)
    sig = models.CharField(max_length=128)  # 签名
    grade = models.IntegerField()  # 教练等级
    is_gender = {
        (1, '男'),
        (2, '女')
    }
    gender = models.BooleanField(choices=is_gender)
    age = models.IntegerField()
    tall = models.FloatField()  # 身高
    weight = models.FloatField()  # 体重

    class Meta:
        db_table = 'coach'


# 教练信息
class Coach_Infor(Base,models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=28)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=128)

    class Meta:

        db_table = 'coachinfor'


