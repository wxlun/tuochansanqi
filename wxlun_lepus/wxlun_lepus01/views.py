from django.shortcuts import render, redirect
from django.http import HttpResponse
from wxlun_lepus01 import models





def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if models.AdminUser.objects.filter(username=username, password=password):
            return redirect('/index.html')
        else:
            return render(request, 'login.html')


def base(request):
        menu_list = []
        temp1='<a href="/index" class="nav-header collapsed" data-toggle="collapse"><i class="glyphicon glyphicon-cloud"></i>仪表盘</i></a>'
        menu_list.append(temp1)
        menu_row = list(
            models.AdminMenu.objects.filter(menu_level=1).values("menu_id","menu_url", "menu_icon","menu_content").order_by("display_order"))
        if menu_row:
            for data in menu_row:
                sbmenu_list = []
                temp = '<a href="/%s" class="nav-header collapsed" data-toggle="collapse"><i class="%s"></i> %s</i></a>' % (data["menu_url"],data["menu_icon"],data["menu_content"])
                menu_list.append(temp)
                pmenu_id = data["menu_id"]
                pmenu_url = data["menu_url"]
                submenu_row = list(
                    models.AdminMenu.objects.filter(menu_level=2,status=1,parent_id=pmenu_id).values("menu_id", "menu_url", "menu_icon",
                                                                         "menu_content").order_by("display_order"))
                if submenu_row:
                    subtempulstart='<ul id="%s" class="nav nav-list   collapse" style="height: 0px;">' %(data["menu_url"])
                    subtempulend = '</ul>'
                    menu_list.append(subtempulstart)
                    for subdata in submenu_row:
                        subtemp = '<li><a href="%s"><i class="%s"></i> %s</a></li>' % (subdata["menu_url"],subdata["menu_icon"],subdata["menu_content"])
                        menu_list.append(subtemp)
                    menu_list.append(subtempulend)
        return {
            "menu_list":menu_list
        }


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
