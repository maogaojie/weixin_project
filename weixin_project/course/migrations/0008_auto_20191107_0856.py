# Generated by Django 2.0.4 on 2019-11-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20191107_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coursestatus',
            field=models.IntegerField(choices=[(1, '人数已满'), (3, '已结束'), (4, '已预约'), (2, '未满')]),
        ),
    ]
