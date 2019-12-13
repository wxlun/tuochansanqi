# Generated by Django 3.0 on 2019-12-04 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbinfo', '0002_auto_20191204_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='dbidc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='机房名字')),
            ],
            options={
                'verbose_name': '机房名称表',
            },
        ),
        migrations.CreateModel(
            name='dbmongodb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, max_length=32, verbose_name='ip地址')),
                ('port', models.IntegerField(db_index=True, max_length=10, verbose_name='端口')),
                ('clsname', models.CharField(max_length=32, verbose_name='集群名称')),
                ('clstype', models.CharField(max_length=32, verbose_name='集群类型')),
            ],
            options={
                'verbose_name': 'MongoDB表',
            },
        ),
        migrations.CreateModel(
            name='dbmongodbcls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clsname', models.CharField(max_length=32, unique=True, verbose_name='集群名称')),
                ('idcwvip', models.CharField(max_length=32, verbose_name='IDC写vip')),
                ('idcrvip', models.CharField(max_length=32, verbose_name='IDC读vip')),
                ('idcvip', models.CharField(max_length=32, verbose_name='IDC外网ip')),
                ('alywvip', models.CharField(max_length=32, verbose_name='aly写vip')),
                ('alyrvip', models.CharField(max_length=32, null=True, verbose_name='aly读vip')),
                ('alyoip', models.CharField(max_length=32, null=True, verbose_name='al外网ip')),
            ],
            options={
                'verbose_name': 'MongoDB集群表',
            },
        ),
        migrations.CreateModel(
            name='dbmysql',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, max_length=32, verbose_name='ip地址')),
                ('port', models.IntegerField(db_index=True, max_length=10, verbose_name='端口')),
                ('role', models.CharField(max_length=32, verbose_name='实例角色')),
                ('db', models.CharField(max_length=1000, verbose_name='库列表')),
                ('dbidc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbinfo.dbidc', verbose_name='外键，父表dbidc')),
            ],
            options={
                'verbose_name': 'MySQL表',
                'unique_together': {('ip', 'port')},
            },
        ),
        migrations.CreateModel(
            name='dbmysqlcls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clsname', models.CharField(max_length=32, unique=True, verbose_name='MySQL集群名称')),
                ('idcwvip', models.CharField(max_length=32, verbose_name='MySQL的IDC写vip')),
                ('idcrvip', models.CharField(max_length=32, verbose_name='IDC读vip')),
                ('idcvip', models.CharField(max_length=32, verbose_name='IDC外网ip')),
                ('alywvip', models.CharField(max_length=32, verbose_name='aly写vip')),
                ('alyrvip', models.CharField(max_length=32, verbose_name='aly读vip')),
                ('alyoip', models.CharField(max_length=32, null=True, verbose_name='al外网ip')),
            ],
            options={
                'verbose_name': 'MySQL集群表',
            },
        ),
        migrations.CreateModel(
            name='dbredis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, max_length=32, verbose_name='ip地址')),
                ('port', models.IntegerField(db_index=True, max_length=10, verbose_name='端口')),
                ('clsname', models.CharField(db_index=True, max_length=32, verbose_name='集群名称')),
                ('clstype', models.CharField(max_length=32, verbose_name='集群类型')),
                ('dbidc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbinfo.dbidc', verbose_name='外键，父表dbidc')),
            ],
            options={
                'verbose_name': 'Redis表',
                'unique_together': {('ip', 'port')},
            },
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
        migrations.AddField(
            model_name='dbmongodb',
            name='dbidc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbinfo.dbmongodbcls', verbose_name='外键，父表dbmongodbcls'),
        ),
        migrations.AlterUniqueTogether(
            name='dbmongodb',
            unique_together={('ip', 'port')},
        ),
    ]