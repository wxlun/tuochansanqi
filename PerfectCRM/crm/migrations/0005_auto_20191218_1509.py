# Generated by Django 3.0 on 2019-12-18 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20191218_1446'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentenrollment',
            unique_together={('customer', 'class_grade')},
        ),
    ]