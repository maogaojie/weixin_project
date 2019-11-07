from django.contrib import admin

# Register your models here.

from course.models import Region, Course, Tag, CourseDetail, CourseType, Store, Coach,Coach_Infor

# Register your models here.
admin.site.register([Region, Course, Tag, CourseDetail, CourseType, Store, Coach,Coach_Infor])
