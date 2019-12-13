from django.shortcuts import render,HttpResponse,redirect
from django import forms
from django.forms import fields
class F1Form(forms.Form):
    user = fields.CharField(max_length=18,min_length=6,required=True)
    pwd = fields.CharField(min_length=6,required=True)
    age = fields.IntegerField(required=True)
    email = fields.EmailField(
        required=True,
        min_length=8,
        error_messages={
            'required':'邮箱不能为空',
            'invalid':'邮箱格式错误',
        }
    )

# Create your views here.


def f1(request):
    if request.method == 'GET':
        obj = F1Form()
        return render(request,'f1.html',{'obj':obj})
    else:
        # u = request.POST.get('user')
        # p = request.POST.get('pwd')
        # e = request.POST.get('email')
        # a = request.POST.get('age')
        # # return render(request,'f1.html')
        # print(u,p,e,a)
        obj = F1Form(request.POST)
        if obj.is_valid():
            print('验证成功',obj.cleaned_data)
            return redirect('http://www.baidu.com')
        else:
            print('验证失败',obj.errors)
            return render(request,'f1.html',{'obj':obj})
