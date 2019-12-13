from django.shortcuts import render,HttpResponse

def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    else:
        user = request.POST.get('user')
        img = request.FILES.get('img')
        print(img.name)
        print(img.size)
        f = open(img.name,'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse('上传成功')
