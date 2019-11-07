from course import models
from rest_framework import serializers


# 课程反序列化
class CourseSerializer(serializers.ModelSerializer):
    # store_id = serializers.ImageField()
    # name = serializers.CharField()
    # money_one = serializers.DecimalField(max_digits=7, decimal_places=2)  # 花费的钱
    # money_two = serializers.IntegerField()  # 花费的课包 1个课包，2两个课包。。。
    # pay_type = serializers.BooleanField()  # 支付方式
    # coach_id = serializers.ImageField()  # 教练
    # course_number = serializers.IntegerField()  # 课程人数
    # star_time = serializers.DateTimeField()  # 开始时间
    # end_time = serializers.DateTimeField()  # 结束时间
    # coursetype_id = serializers.ImageField()  # 课程的类型
    # coursestatus = serializers.IntegerField()  # 课程状态
    # image = serializers.ImageField(upload_to='course')
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


# 课程详情反序列化
class CourseDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = '__all__'


class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ['name','opening_hours','image']
