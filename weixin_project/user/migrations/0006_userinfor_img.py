# Generated by Django 2.0.4 on 2019-11-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191107_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfor',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]