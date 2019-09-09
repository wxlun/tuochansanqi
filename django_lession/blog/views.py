from django.shortcuts import render,HttpResponse,render_to_response
import time
# Create your views here.

def show_time(req):
    # return HttpResponse("Hello")
    t=time.ctime()
    name='tttt'
    # return render(req,"index.html",locals())
    return render(req,"index.html",locals())

# def article_year(req,year,month):
#     return HttpResponse("year:%s month:%s"%(year,month))

def article_year_month(req,year,month):
    return HttpResponse("year:%s month:%s"%(year,month))


def register(req):
    # print(req.path)
    # print(req.get_full_path())
    # return render(req,"register.html")
    return render_to_response("register.html")
