# Generated by Django 2.0.4 on 2019-11-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191113_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycoupon',
            name='status',
            field=models.IntegerField(choices=[(3, '已过期'), (1, '未使用'), (2, '已使用')]),
        ),
    ]
