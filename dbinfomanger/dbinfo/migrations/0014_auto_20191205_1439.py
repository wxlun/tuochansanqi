# Generated by Django 3.0 on 2019-12-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbinfo', '0013_auto_20191205_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbmysqlcls',
            name='alyoip',
            field=models.CharField(max_length=32, verbose_name='al外网ip'),
        ),
    ]