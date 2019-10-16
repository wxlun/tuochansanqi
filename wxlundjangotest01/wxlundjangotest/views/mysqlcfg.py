from django.shortcuts import render, redirect, HttpResponse
from wxlundjangotest import models
import json
from wxlundjangotest.peger import PageInfo


# class PageInfo(object):
#     def __init__(self, current, totalItem, peritems=5):
#    def Custompager(baseurl, currentPage, totalpage):  # 基础页，当前页，总页数



def index(request):
    mysql_list=[]
    # mysql_list = models.MysqlInfo.objects.all().values('id', 'instance_name', 'host', 'port')
    '''
    分页
    '''
    all_count  = models.MysqlInfo.objects.all().count()   # 获取要显示数据库的总数据条数
    page_info = PageInfo(request.GET.get('p'), all_count, '/index.html/',)      # 生成分页对象
    mysql_list = models.MysqlInfo.objects.all().values('id', 'instance_name', 'host', 'port')     # 利用分页对象获取当前页显示数据
    return render(request, 'index.html', {'mysql_list': mysql_list, 'page_info': page_info})     # 模板渲染
    # return render(request, 'index.html', {'mysql_list': mysql_list,'data': data_list, 'page_obj': page_obj,'custompager':custompager})
'''
获取MySQL信息
'''


def get_mysqlinfo(request):
    all_count  = models.MysqlInfo.objects.all().count()   # 获取要显示数据库的总数据条数
    page_info = PageInfo(request.GET.get('page'), all_count, '/get_mysqlinfo/',)      # 生成分页对象
    mysql_list = models.MysqlInfo.objects.all().values('id', 'instance_name', 'host', 'port', 'user', 'passwd').order_by('host','port') [page_info.start_data():page_info.end_data()]    # 利用分页对象获取当前页显示数据
    return render(request, 'mysqlcfg.html', {'mysql_list': mysql_list, 'page_info': page_info})     # 模板渲染

'''
添加MySQL信息
'''


def add_mysql(request):
    response = {'status': True, 'message': None}
    try:
        instance_name = request.POST.get('instance_name')
        host = request.POST.get('host')
        port = request.POST.get('port')
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        models.MysqlInfo.objects.create(
            instance_name=instance_name,
            host=host,
            port=port,
            user=user,
            passwd=passwd
        )
    except Exception as e:
        print(e)
        response['status'] = False
        response['message'] = '用户输入错误'
    result = json.dumps(response, ensure_ascii=False)
    return HttpResponse(result)


'''
删除mysql信息
'''


def del_mysql(request):
    ret = {'status': True}
    try:
        nid = request.GET.get('nid')
        models.MysqlInfo.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


'''
编辑MySQL信息
'''


def edit_mysql(request):
    response = {'code': 1000, 'message': None}
    try:
        id = request.POST.get('id')
        instance_name = request.POST.get('instance_name')
        host = request.POST.get('host')
        port = request.POST.get('port')
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        models.MysqlInfo.objects.filter(id=id).update(
            instance_name=instance_name,
            host=host,
            port=port,
            user=user,
            passwd=passwd
        )
    except Exception as e:
        print(e)
        response['code'] = 1001
        response['message'] = str(e)
    return HttpResponse(json.dumps(response))
