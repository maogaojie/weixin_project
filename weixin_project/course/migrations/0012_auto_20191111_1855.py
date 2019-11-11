# Generated by Django 2.1.4 on 2019-11-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20191111_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coursestatus',
            field=models.IntegerField(choices=[(3, '已结束'), (1, '人数已满'), (4, '已预约'), (2, '未满')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='pay_type',
            field=models.IntegerField(choices=[(1, '课包支付'), (2, '现金支付')]),
        ),
    ]
