# Generated by Django 2.0.4 on 2019-11-13 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('coach_name', models.CharField(max_length=128)),
                ('openid', models.CharField(max_length=128, unique=True)),
                ('sig', models.CharField(max_length=128)),
                ('grade', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')])),
                ('age', models.IntegerField()),
                ('tall', models.FloatField()),
                ('weight', models.FloatField()),
            ],
            options={
                'verbose_name': '教练表',
                'verbose_name_plural': '教练表',
                'db_table': 'coach',
            },
        ),
        migrations.CreateModel(
            name='Coach_Infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('id_number', models.CharField(max_length=28)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=128)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Coach')),
            ],
            options={
                'db_table': 'coachinfor',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('money_one', models.DecimalField(decimal_places=2, max_digits=7)),
                ('money_two', models.IntegerField()),
                ('pay_type', models.IntegerField(choices=[(2, '现金支付'), (1, '课包支付')])),
                ('course_number', models.IntegerField()),
                ('star_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('coursestatus', models.IntegerField(choices=[(1, '人数已满'), (3, '已结束'), (4, '已预约'), (2, '未满')])),
                ('image', models.ImageField(upload_to='course')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Coach')),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_ntroduction', models.CharField(max_length=255)),
                ('training_effect', models.CharField(max_length=255)),
                ('crowd', models.CharField(max_length=255)),
                ('FQA', models.CharField(max_length=255)),
                ('notice', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=True, to='course.Course')),
            ],
            options={
                'db_table': 'coursedetail',
            },
        ),
        migrations.CreateModel(
            name='CourseDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '课程方向表',
                'verbose_name_plural': '课程方向表',
                'db_table': 'coursedirection',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
                'db_table': 'courseType',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('pid', models.IntegerField()),
                ('sname', models.CharField(max_length=128)),
                ('level', models.IntegerField()),
                ('citycode', models.CharField(blank=True, max_length=128, null=True)),
                ('yzcode', models.CharField(blank=True, max_length=128, null=True)),
                ('mername', models.CharField(max_length=128)),
                ('Lng', models.FloatField()),
                ('Lat', models.FloatField()),
                ('pinyin', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '城市表',
                'verbose_name_plural': '城市表',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('opening_hours', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='store')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Region')),
            ],
            options={
                'verbose_name': '店铺表',
                'verbose_name_plural': '店铺表',
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='coursetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseType'),
        ),
        migrations.AddField(
            model_name='course',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseDirection'),
        ),
        migrations.AddField(
            model_name='course',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Store'),
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.ManyToManyField(to='course.Tag'),
        ),
        migrations.AddField(
            model_name='coach',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Store'),
        ),
    ]
