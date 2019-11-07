from django.contrib import admin
from user.models import User,UserInfor
#
# # Register your models here.
admin.site.register([User, UserInfor])
