from course import models
from rest_framework import serializers


# 课程反序列化
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tag')

        course = models.Course.objects.create(**validated_data)
        for tag in tags:
            tag = models.Tag.objects.filter(id=tag.id).first()
            course.tag.add(tag)
            course.save()
        return course


# 课程序列化
class CourseModelSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.name')
    pay_type = serializers.CharField(source='pay')
    coach = serializers.CharField(source='coach.coach_name')
    coursetype = serializers.CharField(source='coursetype.name')
    coursestatus = serializers.CharField(source='status')
    tag = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = '__all__'

    def get_tag(self, obj):
        query_set = obj.tag.all()
        return [{'name': obj.name} for obj in query_set]


# 课程详情
class CourseDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = '__all__'


# 门店
class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ['name', 'opening_hours', 'image']


# 教练
class CoachModelSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.name')
    gender = serializers.CharField(source='is_gender')

    class Meta:
        model = models.Coach
        fields = ['store','coach_name', 'sig', 'grade', 'gender', 'age', 'tall', 'weight']


# 方向
class DirectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDirection
        fields = '__all__'
