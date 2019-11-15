from django.contrib import admin

# Register your models here.

from orders.models import Coupon,MyCoupon,Order


admin.site.register([Coupon,MyCoupon,Order])
