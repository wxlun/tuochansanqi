from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def addbook(request):
    Book.objects.create(name='python基础',price=10,pub_date='2017-01-01',author='wxlun')
    return HttpResponse("添加成功")

def update(request):
    Book.objects.filter(name="go").update(price=100)
    return HttpResponse("修改成功")

def delete(request):
    Book.objects.filter(name="go").delete()
    return HttpResponse("删除成功")

def select(request):
    book_list=Book.objects.all()[:3]
    return render(request,"index.html",{"book_list":book_list})
