# Generated by Django 2.1.4 on 2019-11-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')]),
        ),
    ]
