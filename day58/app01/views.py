from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

USER_LIST = []
for i in range(1, 666):
    temp = {'name': 'root' + str(i), 'age': i}
    USER_LIST.append(temp)


class CustomPaginator(Paginator):
    def __init__(self, current_page, per_pager_num, *args, **kwargs):
        self.current_page = int(current_page)
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def pager_num_range(self):
        if self.num_pages < self.per_page_item_num:
            return range(1, self.num_pages + 1)
        part = int(self.per_page_item_num / 2)
        if self.current_page <= part:
            return range(1, self.per_page_item_num + 1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages - self.per_page_item_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)


def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)
    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    data = USER_LIST[start:end]
    if current_page <= 1:
        up_pager = 1
    up_pager = current_page - 1
    down_pager = current_page + 1
    return render(request, 'index.html', {'user_list': data, 'up_pager': up_pager, 'down_pager': down_pager})


def index1(request):
    current_page = request.GET.get('p')
    paginator = CustomPaginator(current_page, 11, USER_LIST, 10)

    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象

    try:
        posts = paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index1.html', {'posts': posts})


def index2(request):
    from app01.pager import Pagination
    current_page = request.GET.get('p')
    page_obj = Pagination(666, current_page)
    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request, 'index2.html', {'data': data_list, 'page_obj': page_obj})
