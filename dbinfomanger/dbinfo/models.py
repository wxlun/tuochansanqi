from django.db import models

class user(models.Model):
    name = models.CharField(max_length=32,null=False,verbose_name='用户名')
    password = models.CharField(max_length=100,null=False,verbose_name='密码')
    class Meta:
        verbose_name = '用户表'

class dbidc(models.Model):
    name = models.CharField(max_length=32,null=False,unique=True,verbose_name="机房名字")
    class Meta:
        verbose_name = '机房名称表'

class dbmysqlcls(models.Model):
    clsname = models.CharField(max_length=32,null=False,verbose_name='MySQL集群名称',unique=True)
    port = models.IntegerField(max_length=10,null=False,verbose_name='端口',db_index=True)
    idcwvip = models.CharField(max_length=32,null=False,verbose_name='MySQL的IDC写vip')
    idcrvip = models.CharField(max_length=32,null=False,verbose_name='IDC读vip')
    idcoip = models.CharField(max_length=32,null=False,verbose_name='IDC外网ip')
    idctip = models.CharField(max_length=32,null=False,verbose_name='IDC同步ip')
    alywvip = models.CharField(max_length=32,null=False,verbose_name='aly写vip')
    alyrvip = models.CharField(max_length=32,null=False,verbose_name='aly读vip')
    alyoip = models.CharField(max_length=32,null=False,verbose_name='al外网ip')
    alytip = models.CharField(max_length=32,null=False,verbose_name='aly同步ip')
    class Meta:
        verbose_name = "MySQL集群表"

class dbmongodbcls(models.Model):
    clsname = models.CharField(max_length=32,null=False,verbose_name='集群名称',unique=True)
    idcwvip = models.CharField(max_length=32,null=False,verbose_name='IDC写vip')
    idcrvip = models.CharField(max_length=32,null=False,verbose_name='IDC读vip')
    idctip = models.CharField(max_length=32,null=False,verbose_name='IDC同步ip')
    idcoip = models.CharField(max_length=32,null=False,verbose_name='IDC外网ip')
    alywvip = models.CharField(max_length=32,null=False,verbose_name='aly写vip')
    alyrvip = models.CharField(max_length=32,null=True,verbose_name='aly读vip')
    alyoip = models.CharField(max_length=32,null=True,verbose_name='al外网ip')
    alytip = models.CharField(max_length=32,null=False,verbose_name='aly同步ip')

    class Meta:
        verbose_name = "MongoDB集群表"


class dbmysql(models.Model):
    ip = models.CharField(max_length=32,null=False,verbose_name='ip地址',db_index=True)
    port = models.IntegerField(max_length=10,null=False,verbose_name='端口',db_index=True)
    dbcls = models.ForeignKey(dbmysqlcls,verbose_name='外键，父表dbmysqlcls',db_index=True,on_delete=models.CASCADE)
    dbidc = models.ForeignKey(dbidc,verbose_name='外键，父表dbidc',db_index=True,on_delete=models.CASCADE)
    role = models.CharField(max_length=32,null=False,verbose_name='实例角色')
    db = models.CharField(max_length=1000,null=False,verbose_name='库列表')
    class Meta:
        unique_together = ["ip","port"]
        verbose_name = "MySQL表"

class dbredis(models.Model):
    ip = models.CharField(max_length=32,null=False,verbose_name='ip地址',db_index=True)
    port = models.IntegerField(max_length=10,null=False,verbose_name='端口',db_index=True)
    clsname = models.CharField(max_length=32,null=False,verbose_name='集群名称',db_index=True)
    clstype = models.CharField(max_length=32,null=False,verbose_name='集群类型')
    dbidc = models.ForeignKey(dbidc,verbose_name='外键，父表dbidc',on_delete=models.CASCADE)
    class Meta:
        unique_together = ["ip","port"]
        verbose_name = 'Redis表'

class dbmongodb(models.Model):
    ip = models.CharField(max_length=32,null=False,verbose_name='ip地址',db_index=True)
    port = models.IntegerField(max_length=10,null=False,verbose_name='端口',db_index=True)
    clsname = models.CharField(max_length=32,null=False,verbose_name='集群名称')
    clstype = models.CharField(max_length=32,null=False,verbose_name='集群类型')
    dbidc = models.ForeignKey(dbidc,verbose_name='外键，父表dbidc',on_delete=models.CASCADE)
    dbidc = models.ForeignKey(dbmongodbcls,verbose_name='外键，父表dbmongodbcls',on_delete=models.CASCADE)
    class Meta:
        unique_together = ["ip","port"]
        verbose_name = 'MongoDB表'


class usercollection(models.Model):
    ip = models.CharField(max_length=32,null=False)
    port = models.IntegerField(max_length=10,null=False,verbose_name='端口',db_index=True)
    username = models.CharField(max_length=32,blank=True,null=True)
    hostname = models.CharField(max_length=32,blank=True,null=True)
    class Meta:
        unique_together = ["ip","port",'username','hostname']
