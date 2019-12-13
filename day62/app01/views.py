from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def ajax1(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse('...')