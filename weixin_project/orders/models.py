from django.db import models

# Create your models here.

# 优惠卷
from course.models import Store
from user.models import User


class Coupon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'coupon'
        verbose_name_plural = '优惠券'

    def __str__(self):
        return self.name






class MyCoupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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







