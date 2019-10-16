# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dbuser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dbuser'


class MysqlInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_name = models.CharField(max_length=30, blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=30)
    user = models.CharField(max_length=10, blank=True, null=True)
    passwd = models.CharField(max_length=50, blank=True, null=True)
    is_master = models.IntegerField(blank=True, null=True)
    is_slave = models.IntegerField(blank=True, null=True)
    dbcount = models.BigIntegerField(blank=True, null=True)
    tablecount = models.BigIntegerField(blank=True, null=True)
    dblist = models.TextField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mysql_info'
        unique_together = (('host', 'port'),)


class MysqlVariables(models.Model):
    id = models.BigAutoField(primary_key=True)
    vname = models.CharField(max_length=30)
    vvalue = models.CharField(max_length=30)
    host = models.CharField(max_length=30)
    post = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mysql_variables'
