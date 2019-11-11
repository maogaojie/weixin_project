# Generated by Django 2.1.4 on 2019-11-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20191111_1855'),
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
            field=models.IntegerField(choices=[(4, '已预约'), (3, '已结束'), (1, '人数已满'), (2, '未满')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='pay_type',
            field=models.IntegerField(choices=[(2, '现金支付'), (1, '课包支付')]),
        ),
    ]
