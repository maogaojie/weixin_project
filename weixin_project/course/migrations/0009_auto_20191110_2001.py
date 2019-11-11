# Generated by Django 2.1.4 on 2019-11-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20191110_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.IntegerField(choices=[(2, '女'), (1, '男')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='coursestatus',
            field=models.IntegerField(choices=[(2, '未满'), (4, '已预约'), (3, '已结束'), (1, '人数已满')]),
        ),
    ]
