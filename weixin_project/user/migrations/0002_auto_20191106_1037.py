# Generated by Django 2.0.4 on 2019-11-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.BooleanField(choices=[(1, '男'), (2, '女')]),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='gender',
            field=models.BooleanField(choices=[(1, '男'), (2, '女')]),
        ),
    ]
