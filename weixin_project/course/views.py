from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from course import serializer
from course import models


class GetCourse(APIView):
    """
    获取所有课程信息
    """
    def get(self, request):
        mes = {}
        course_list = models.Course.objects.all()
        course_list = serializer.CourseModelSerializer(course_list, many=True)
        mes['code'] = 200
        mes['course_list'] = course_list.data
        return Response(mes)
