# Generated by Django 2.0.4 on 2019-11-06 10:34

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
                ('openid', models.CharField(max_length=128)),
                ('sig', models.CharField(max_length=128)),
                ('grade', models.IntegerField()),
                ('gender', models.BooleanField(choices=[(2, '女'), (1, '男')])),
                ('age', models.IntegerField()),
                ('tall', models.FloatField()),
                ('weight', models.FloatField()),
            ],
            options={
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
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Coach')),
            ],
            options={
                'db_table': 'coachinfor',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('openid', models.IntegerField()),
                ('username', models.CharField(max_length=128)),
                ('invitation_code', models.CharField(max_length=128)),
                ('invitation_num', models.IntegerField(default=0)),
                ('succeed_invitation', models.IntegerField(default=0)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=128)),
                ('gender', models.BooleanField(choices=[(2, '女'), (1, '男')])),
                ('birthday', models.DateField()),
                ('tall', models.FloatField()),
                ('weight', models.FloatField()),
                ('BMI', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'userinfor',
            },
        ),
    ]
