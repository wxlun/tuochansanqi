from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def acc_login(request):
    error_msg = ""
    if request.method == 'POST':
        error_msg = ""
        username = request.POST.get("username")
        password = request.POST.get("password")
        """验证用户名密码"""
        user = authenticate(username=username,password=password)
        if user:
            print("passed authencation",user)
            """生成session，登录"""
            login(request,user)
            # """如果有next，否则跳转到首页"""
            # return redirect(request.GET.get('next','/'))
            return redirect('/crm/')

        else:
            error_msg = "Wrong username or password!"
    return render(request,'login.html',{"error_msg":error_msg})

def acc_logout(request):
    logout(request)
    return redirect("/login/")
