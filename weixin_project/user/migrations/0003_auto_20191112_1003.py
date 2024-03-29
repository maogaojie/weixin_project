# Generated by Django 2.1.4 on 2019-11-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfor',
            name='status',
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='day',
            field=models.IntegerField(choices=[(1, '2天'), (2, '3天'), (3, '4天'), (4, '5天')]),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='hope',
            field=models.IntegerField(choices=[(2, '增肌塑形'), (1, '减脂塑性'), (3, '体态改善')]),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='how_long',
            field=models.IntegerField(choices=[(2, '60分钟'), (1, '45分钟'), (3, '90分钟'), (4, '105分钟')]),
        ),
    ]
