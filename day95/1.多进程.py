"""
可以实现并发，但是，进程有等待响应的时间
方式一：直接返回处理
方式二：通过回调函数处理
"""
##################编写方式一#####################
"""
from concurrent.futures import ProcessPoolExecutor
import requests

def task(url):
    response = requests.get(url)
    print(url,response)

pool = ProcessPoolExecutor(8)

url_list = [
    'http://www.baidu.com',
    'http://www.vancl.com',
    'http://www.hc360.com',
    'http://www.sina.com.cn',
    'http://www.zhihu.com',
    'http://www.bing.com',
    'http://www.vmall.com',
    'http://www.jd.com'
]

for url in url_list:
    pool.submit(task,url)

pool.shutdown(wait=True)
"""


##################编写方式二#####################
from concurrent.futures import ProcessPoolExecutor
import requests

def task(url):
    """
    下载页面
    :param url:
    :return:
    """
    response = requests.get(url)
    return response

def done(future,*args,**kwargs):
    response = future.result()
    print(response.status_code,response.content)


pool = ProcessPoolExecutor(8)

url_list = [
    'http://www.baidu.com',
    'http://www.vancl.com',
    'http://www.hc360.com',
    'http://www.sina.com.cn',
    'http://www.zhihu.com',
    'http://www.bing.com',
    'http://www.vmall.com',
    'http://www.jd.com'
]

for url in url_list:
    v= pool.submit(task,url)
    v.add_done_callback(done)

pool.shutdown(wait=True)