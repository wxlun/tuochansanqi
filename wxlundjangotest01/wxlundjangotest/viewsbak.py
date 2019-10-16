from django.shortcuts import render, redirect
from django.http import HttpResponse
from wxlundjangotest.models import *
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html')


"""
登录跳转
"""


def login(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    if Dbuser.objects.filter(Q(name=user) & Q(pwd=pwd)):
        return redirect("/index/")
        # return HttpResponse("登录成功")
    else:
        return render(request, "login.html")


def dbinfoselect(request):
    ip = request.POST.get("ip")
    port = request.POST.get("port")
    dict = {}
    if ip:
        dict["host"] = ip
    if port:
        dict["port"] = port

    # infolistselect=MysqlInfo.objects.filter(Q(host=ip)&Q(port=port)).values("host","port","instance_name","dbcount","tablecount")
    infolistselect = MysqlInfo.objects.filter(**dict).values("host", "port", "instance_name", "dbcount", "tablecount")
    return render(request, "selectres.html", {"infolistselect": infolistselect})


def add_dbinfo(request):
    # if request.method=="POST":
    # instance_name=request.POST.get("instance_name")
    # host=request.POST.get("host")
    # post=request.POST.get("post")
    # MysqlInfo.objects.create(instance_name=instance_name,)
    return render(request, 'add_dbinfo.html')

    # else:
    #     redirect('/dbinfoselect/')
