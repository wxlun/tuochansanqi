from django.shortcuts import render
from django.db import models
def filter(request,*args,**kwargs):
  if request.method=="GET":
    condition={}
    for k,v in kwargs.items():
          kwargs[k]=int(v) #模板if判断row.id是数字，所以这里需要转换
          if v=="0":#当条件为0代表所选的是全部，那么就不必要加入到过滤条件中
            pass
          else:
            condition[k]=int(v)
    aritcle=models.Article.objects.filter(**condition)
    aritcle_type=models.Article_type.objects.all()
    aritcle_category=models.Category.objects.all()
    return render(request,'search.html',{
      'aritcle':aritcle,
      'article_type':aritcle_type,
      'article_category':aritcle_category,
      'article_arg':kwargs,#将当前的筛选条件传递给html
    })