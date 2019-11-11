# Generated by Django 2.1.4 on 2019-11-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20191110_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coursestatus',
            field=models.IntegerField(choices=[(2, '未满'), (3, '已结束'), (4, '已预约'), (1, '人数已满')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='pay_type',
            field=models.IntegerField(choices=[(2, '现金支付'), (1, '课包支付')]),
        ),
    ]