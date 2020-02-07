from django.db import models

class ServiceIndex(models.Model):
    name = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    data_type_choices = (
        ('int','int'),
        ('float','float'),
        ('str','string')
    )
    date_type = models.CharField('指标数据类型',max_length=32,choices=data_type_choices,default='int')
    memo = models.CharField('备注',max_length=128,blank=True,null=True)
    def __str__(self):
        return "%s.%s" %(self.name,self.key)

class Service(models.Model):
    name = models.CharField('服务名称',max_length=64,unique=True)
    interval = models.IntegerField('监控间隔',default=60)
    plugin_name = models.CharField('插件名',max_length=64,default='n/a')
    items = models.ManyToManyField('ServiceIndex',verbose_name='指标列表',blank=True)
    memo = models.CharField('备注',max_length=128,blank=True,null=True)
    def __str__(self):
        return self.name
    # def get_service_items(obj):
    #     return ",".join(i.name for i in obj.items.all())


class Template(models.Model):
    name = models.CharField('模板名称',max_length=64,unique=True)
    services = models.ManyToManyField('Service',verbose_name='服务列表')
    triggers = models.ManyToManyField('Trigger',verbose_name='触发器列表',blank=True)
    def __str__(self):
        return self.name

class Trigger(models.Model):
    name = models.CharField('触发器名称',max_length=64)
    expression = models.TextField('表达式')
    serverity_choices = (
        (1,'Information'),
        (2,'Warning'),
        (3,'Average'),
        (4,'High'),
        (5,'diaster'),
    )
    serverity = models.IntegerField('告警级别',choices=serverity_choices)
    enabled = models.BooleanField(default=True)
    memo = models.TextField('备注',blank=True,null=True)
    def __str__(self):
        return self.name

class Host(models.Model):
    name = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True)
    templates = models.ManyToManyField("Template",blank=True)
    monitored_by_choices = (
        ('agent','Agent'),
        ('snmp','SNMP'),
        ('wget','WGET'),
    )
    monitored_by = models.CharField('监控方式',max_length=64,choices=monitored_by_choices)
    status_choices = (
        (1,'Online'),
        (2,'Down'),
        (3,'Unreacchable'),
        (4,'Offline'),
    )
    status = models.IntegerField('状态',choices=status_choices,default=1)
    memo = models.TextField('备注',blank=True,null=True)
    def __str__(self):
        return self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    templates = models.ManyToManyField("Template",blank=True)
    memo = models.TextField('备注',blank=True,null=True)
    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=64,unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True)
    hosts = models.ManyToManyField('host',blank=True)
    conditions = models.TextField('告警条件')
    interval = models.IntegerField('告警间隔(2s)',default=300)
    operations = models.ManyToManyField('ActionOperation')
    recover_notice = models.BooleanField('故障恢复后发送通知消息',default=True)
    recover_subject = models.CharField(max_length=128,blank=True,null=True)
    recover_message = models.TextField(blank=True,null=True)
    enabled = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ActionOperation(models.Model):
    name = models.CharField(max_length=64)
    step = models.SmallIntegerField('第n次告警',default=1)
    action_type_choices = (
        ('email','Email'),
        ('sms','SMS'),
        ('script','RunScript'),
    )
    action_type = models.CharField('动作类型',choices=action_type_choices,default='email',max_length=64)
    # notifiers = models.ManyToManyField(host_models.UserProfile,verbose_name='通知对象',blank=True)
    def __str__(self):
        return self.name

class Maintenance(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField('Host',blank=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True)
    content = models.TextField('维护内容')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return self.name



