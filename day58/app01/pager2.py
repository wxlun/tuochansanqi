class Pagination1(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=30, maxPageNum=7):
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum
        def start(self):
            return (self.current_page - 1) * self.per_page_item_num

        def end(self):
            return self.current_page * self.per_page_item_num

        @property
        def num_pages(self):
            a, b = divmod(self.total_count, self.per_page_item_num)
            if b == 0:
                return a
            return a + 1

        def pager_num_range(self):
            if self.num_pages < self.max_page_num:
                return range(1, self.num_pages + 1)
            part = int(self.max_page_num / 2)
            if self.current_page <= part:
                return range(1, self.max_page_num + 1)
            if (self.current_page + part) > self.num_pages:
                return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
            return range(self.current_page - part, self.current_page + part + 1)

        def page_str(self):
            page_list = []
            first = "<a href='/index2.html?p=1'>首页</a>"
            page_list.append(first)
            if self.current_page == 1:
                prev = "<a href='#'>上一页</a>"
            else:
                prev = "<a href='/index2.html?p=%s'>上一页</a>" % (self.current_page - 1,)
            page_list.append(prev)

            for i in self.pager_num_range():
                if i == self.current_page:
                    temp = "<a style='font-size:30px;' href='/index2.html?p=%s'>%s</a>" % (i, i)
                else:
                    temp = "<a href='/index2.html?p=%s'>%s</a>" % (i, i)

                page_list.append(temp)

            if self.current_page == self.num_pages:
                nex = "<a href='#'>下一页</a>"
            else:
                nex = "<a href='/index2.html?p=%s'>下一页</a>" % (self.current_page + 1,)
                page_list.append(nex)
            last = "<a href='/index2.html?p=%s'>尾页</a>" % (self.num_pages,)
            page_list.append(first)
            return ''.join(page_list)
