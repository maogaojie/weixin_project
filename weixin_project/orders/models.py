from django.db import models

# Create your models here.
from course.models import Store, Course, Coach
from user.models import User


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


# 优惠卷
class Coupon(models.Model):
    # store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    money = models.DecimalField(max_digits=7,decimal_places=2)

    class Meta:
        db_table = 'coupon'
        verbose_name_plural = '优惠券'

    def __str__(self):
        return self.name


# 我的优惠卷
class MyCoupon(Base, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    number = models.IntegerField()
    expiration_time = models.DateTimeField()
    is_status = {
        (1, '未使用'),
        (2, '已使用'),
        (3, '已过期')
    }
    status = models.IntegerField(choices=is_status)

    class Meta:
        db_table = 'mycoupon'
        verbose_name_plural = '我的优惠卷'

    def __str__(self):
        return self.name


# 订单表
class Order(Base, models.Model):
    order_number = models.CharField(max_length=255)  # 订单编号
    money = models.CharField(max_length=15)  # 金额
    course = models.ForeignKey(Course, on_delete=True)  # 课程
    user = models.ForeignKey(User, on_delete=True)  # 用户
    code = models.CharField(max_length=10)  # 到店验证码
    coach = models.ForeignKey(Coach, on_delete=True)  # 教练
    is_coupon = models.BooleanField(default=False)  # 是否使用优惠卷
    mycoupon = models.ForeignKey(MyCoupon, on_delete=models.SET_NULL, blank=True, null=True)  # 优惠卷

    class Meta:
        db_table = 'orders'
        verbose_name_plural = '订单表'
