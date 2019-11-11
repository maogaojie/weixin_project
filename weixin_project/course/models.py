from django.db import models


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


# 精准地址
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)  # 加后缀名 省市区
    pid = models.IntegerField()
    sname = models.CharField(max_length=128)  # 不加后缀
    level = models.IntegerField()  # 等级
    citycode = models.CharField(max_length=128, null=True, blank=True)  # 城市区号
    yzcode = models.CharField(max_length=128, null=True, blank=True)  # 城市邮编
    mername = models.CharField(max_length=128)  # 所在地区联名 (中国,北京,北京市)
    Lng = models.FloatField()  # 经度
    Lat = models.FloatField()  # 纬度
    pinyin = models.CharField(max_length=128)

    class Meta:
        db_table = 'region'
        verbose_name = '城市表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseType(models.Model):
    name = models.CharField(max_length=128)  # 课程分类名称

    class Meta:
        db_table = 'courseType'
        verbose_name = '课程分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 店铺表
class Store(models.Model):
    city = models.ForeignKey(Region, on_delete=models.CASCADE)  # 地址
    name = models.CharField(max_length=128)  # 店名
    opening_hours = models.CharField(max_length=128)  # 营业时间
    image = models.ImageField(upload_to='store')

    class Meta:
        db_table = 'store'
        verbose_name = '店铺表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教练
class Coach(Base, models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    coach_name = models.CharField(max_length=128)
    openid = models.CharField(max_length=128, unique=True)
    sig = models.CharField(max_length=128)  # 签名
    grade = models.IntegerField()  # 教练等级
    is_gender = {
        (1, '男'),
        (2, '女')
    }
    gender = models.IntegerField(choices=is_gender)
    age = models.IntegerField()
    tall = models.FloatField()  # 身高
    weight = models.FloatField()  # 体重

    class Meta:
        db_table = 'coach'
        verbose_name = '教练表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.coach_name


# 课程方向
class CourseDirection(models.Model):
    name = models.CharField(max_length=128)  # 舞蹈。。搏击。。

    class Meta:
        db_table = 'coursedirection'
        verbose_name = '课程方向表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程表
class Course(Base, models.Model):
    direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)  # 舞蹈。。搏击。。
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    money_one = models.DecimalField(max_digits=7, decimal_places=2)  # 花费的钱
    money_two = models.IntegerField()  # 花费的课包 1个课包，2两个课包。。。
    pay = {
        (1, '课包支付'),
        (2, '现金支付')
    }
    pay_type = models.IntegerField(choices=pay)  # 支付方式
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)  # 教练
    course_number = models.IntegerField()  # 课程人数
    star_time = models.DateTimeField()  # 开始时间
    end_time = models.DateTimeField()  # 结束时间
    coursetype = models.ForeignKey(CourseType, on_delete=models.CASCADE)  # 课程的类型
    status = {
        (1, '人数已满'),
        (2, '未满'),
        (3, '已结束'),
        (4, '已预约'),
    }
    coursestatus = models.IntegerField(choices=status)  # 课程状态
    image = models.ImageField(upload_to='course')
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'course'
        verbose_name = '课程表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseDetail(models.Model):
    course = models.ForeignKey(Course, on_delete=True)
    course_ntroduction = models.CharField(max_length=255)  # 课程介绍
    training_effect = models.CharField(max_length=255)  # 训练效果
    crowd = models.CharField(max_length=255)  # 适合人群
    FQA = models.CharField(max_length=255)  # FQA
    notice = models.CharField(max_length=255)  # 注意事项

    class Meta:
        db_table = 'coursedetail'


# 教练信息
class Coach_Infor(Base, models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=28)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=128)

    class Meta:
        db_table = 'coachinfor'
