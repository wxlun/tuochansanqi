from django.shortcuts import render,redirect

# Create your views here.


def login(request):
    print("COOKIES",request.COOKIES)
    print("SESSION",request.session)
    if request.method=="POST":
        name=request.POST.get("user")
        pwd = request.POST.get("pwd")
        if name == "yuan" and pwd=="123":
            # ret=redirect("/index/")
            # ret.set_cookie("username",name)
            # return ret

            request.session["is_login"]=True
            request.session["user"]=name

            return redirect("/index/")

    return render(request,"login.html")

def index(request):
    # if request.COOKIES.get("suibian",None):
    #     name ="yuan"
    #     return render(request,"index.html",locals())

    if request.session.get("is_login",None):
        name=request.session.get("user",None)
        return render(request,"index.html",locals())
    else:
        return redirect("/login/")