# Generated by Django 2.0.4 on 2019-11-06 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='city',
            name='update_time',
        ),
    ]
