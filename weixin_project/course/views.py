from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from course import serializer
from course import models
from utils.baidu import get_address


class GetCourseAPIView(APIView):
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


class PrivateCourse(APIView):
    """
    获取私教课程
    """
    def get(self,request):
        mes = {}
        store_id = request.GET.get('store_id')
        course_list = models.Course.objects.filter(store_id=store_id,course_type=2).all()
        course_list = serializer.CourseModelSerializer(course_list,many=True)
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
    """
    获取地理位置
    门店信息
    """

    def post(self, request):
        lat = request.data['lat']  # 纬度
        lng = request.data['lng']  # 经度
        mes = get_address(lat, lng)
        return Response(mes)


class GetCoachAPIView(APIView):
    """
    获取当前门店教练信息
    """

    def post(self, request):
        store_id = request.data['store_id']
        coach = models.Coach.objects.filter(store_id=store_id).all()
        coach = serializer.CoachModelSerializer(coach, many=True)
        mes = {}
        mes['code'] = 200
        mes['coach_list'] = coach.data
        return Response(mes)


class GetCourseDirection(APIView):
    """
     获取课程方向(舞蹈，搏击。。)

    """

    def get(self, request):
        mes = {}
        direction = models.CourseDirection.objects.all()
        direction = serializer.DirectionModelSerializer(direction, many=True)
        mes['code'] = 200
        mes['direction'] = direction.data
        return Response(mes)


class DirectionAPIView(APIView):
    """
    获取一个方向的课程
    """

    def post(self, request):
        mes = {}
        course = models.Course.objects.filter(direction_id=request.data['id']).all()
        course = serializer.CourseModelSerializer(course, many=True)
        mes['code'] = 200
        mes['course_list'] = course.data
        return Response(mes)

