from django.shortcuts import render,HttpResponse
import time,_datetime
# Create your views here.

def show_time(request):
    t=_datetime.datetime.now()
    return  render(request,'show_time.html',{"time":t})

    # return HttpResponse("<html><body> It is now %s.</body></html>" %t)