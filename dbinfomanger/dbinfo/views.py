from django.shortcuts import render,redirect
from dbinfo import models

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name)
        print(password)
        if models.user.objects.filter(name=name,password=password):
            return redirect('/index.html')
        else:
            return render(request,'login.html')


def index(request):
    if request.method == "GET":
        mysql_list = models.dbmysql.objects.filter().values('ip','port','role','db','dbcls__clsname','dbidc__name')
        mysql_count = models.dbmysql.objects.count()
        mongodb_count = models.dbmongodb.objects.count()
        redis_count = models.dbredis.objects.count()
        return render(request,'index.html',{"mysql_list":mysql_list,"mysql_count":mysql_count,"mongodb_count":mongodb_count,"redis_count":redis_count})

    else:
        pass


def mysql_cls(request):
    if request.method == "GET":
        mysqlcls_list = models.dbmysqlcls.objects.filter().values('clsname','port','idcwvip','idcrvip','idcoip','idctip','alywvip','alyrvip','alyoip','alytip')
        print(mysqlcls_list)
        return render(request,'mysql_cls.html',{"mysqlcls_list":mysqlcls_list})

    else:
        pass

def mysql_info(request):
    if request.method == "GET":
        mysql_list = models.dbmysql.objects.filter().values('ip','port','role','db','dbcls__clsname','dbidc__name').order_by('dbcls__clsname','ip','port')
        return render(request,'mysql_info.html',{"mysql_list":mysql_list})

    else:
        pass