from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from course import serializer
from course import models
from utils.baidu import get_address


class GetCourse(APIView):
    """
    获取所有课程信息
    """

    def get(self, request):
        print('1111111111')
        mes = {}
        course_list = models.Course.objects.all()
        course_list = serializer.CourseModelSerializer(course_list, many=True)
        mes['code'] = 200
        mes['course_list'] = course_list.data
        return Response(mes)


class GetCourseDetail(APIView):
    """
    获取课程详情
    """

    def get(self, request):
        mes = {}
        id = request.GET.get('id')
        course = models.CourseDetail.objects.filter(course_id=id).first()
        course_detail = serializer.CourseDetailModelSerializer(course, many=False)
        mes['code'] = 200
        mes['data'] = course_detail.data
        return Response(mes)


class GetStoreAPIView(APIView):
    def get(self, request):
        lat = request.GET.get('lat')  # 纬度
        lng = request.GET.get('lng')  # 经度
        mes = get_address(lat, lng)
        return Response(mes)

