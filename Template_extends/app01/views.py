from django.shortcuts import render

# Create your views here.

def backend(request):
    return render(request,'base.html')

def student(req):
    student_list=['piter','lucy','KG']
    return render(req,"student2.html",locals())