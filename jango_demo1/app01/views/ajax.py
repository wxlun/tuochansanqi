from django.shortcuts import render,HttpResponse

def ajax1(request):
    return render(request,'ajax1.html')

def ajax2(request):
    user=request.GET.get('username')
    pwd=request.GET.get('password')
    import time
    time.sleep(5)
    return HttpResponse('12345')

from app01 import models
def ajax4(request):
    nid = request.GET.get('nid')
    msg='成功'
    try:
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        msg=str(e)

    return HttpResponse(msg)
