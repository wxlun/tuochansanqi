from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.

from django.db.models import Avg,Sum,Min,Max
def index(request):
    return render(request,"index.html")

def addbook(request):
    # Book.objects.create(name="linux运维",price=77,pub_date="2017-12-12",publish_id=2)
    # publish_obj=Publish.objects.filter(name="人民出版社")[0]
    # Book.objects.create(name="GO",price=23,pub_date="2017-05-12",publish=publish_obj)
    # book_obj=Book.objects.get(name="python")
    # print(book_obj.name)
    # print(book_obj.pub_date)
    # print(book_obj.publish.name)
    # print(book_obj.publish.city)

    # pub_obj=Publish.objects.filter(name="人民出版社")[0]
    # ret=Book.objects.filter(publish=pub_obj).values("name","price")
    # print(ret)
    #
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # print(pub_obj.book_set.all().values("name","price"))
    # rest=Book.objects.filter(publish__name="人民出版社").values("name","price")
    # print(rest)
    # rest2=Publish.objects.filter(book__name="python").values("name")
    # print(rest2)
    # rest3=Book.objects.filter(name="python").values("publish__name")
    # print(rest3)
    #

    # book_obj=Book.objects.get(id=3)
    # print(book_obj.authors.all())
    # print(type(book_obj.authors.all()))
    #
    # author_obj=Author.objects.get(id=2)
    # print(author_obj.book_set.all())
    #
    # book_obj=Book.objects.get(id=4)
    # author_objs=Author.objects.all()
    # #book_obj.authors.add(*author_objs)
    # book_obj.authors.remove(*author_objs)


    reg=Book.objects.all().aggregate(abc=Sum("price"))
    print(reg)



    return HttpResponse("55555")



def update():pass
def delete():pass
def select():pass