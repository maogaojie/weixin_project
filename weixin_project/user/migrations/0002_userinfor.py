# Generated by Django 2.1.4 on 2019-11-12 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20191112_0946'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=128)),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')])),
                ('birthday', models.DateField()),
                ('tall', models.FloatField()),
                ('weight', models.FloatField()),
                ('BMI', models.FloatField()),
                ('aim_weight', models.FloatField()),
                ('hope', models.IntegerField(choices=[(3, '体态改善'), (1, '减脂塑性'), (2, '增肌塑形')])),
                ('day', models.IntegerField(choices=[(1, '2天'), (4, '5天'), (3, '4天'), (2, '3天')])),
                ('how_long', models.IntegerField(choices=[(2, '60分钟'), (4, '105分钟'), (1, '45分钟'), (3, '90分钟')])),
                ('status', models.IntegerField(choices=[(2, '已预约'), (1, '未预约')], default=1)),
                ('tag', models.ManyToManyField(to='course.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name_plural': '用户信息计划表',
                'db_table': 'userinfor',
            },
        ),
    ]
