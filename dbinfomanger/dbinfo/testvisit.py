#_*_coding:utf-8_*_
__author__ = 'wxlun'


from dbinfo import testcommon


# def run():
#     inp = input('请输入你想访问的url：').strip()
#     if inp == "login":
#         testcommon.login()
#     elif inp == "logout":
#         testcommon.logout()
#     elif inp == "home":
#         testcommon.home()
#     else:
#         print("404")
# def run():
#     inp = input('请输入你想访问的url：').strip()
#     if hasattr(testcommon,inp):
#         f=getattr(testcommon,inp)
#         f()
#
# if __name__ == '__main__':
#     run()

# def print2out(fun1):
#     def print2():
#         return 2
#     return print2
# @print2out
# def print1():
#     return '123'
# print(print1())
#


def outer(x):
    def inner():
        return '戴了inner牌帽子的 ' + x()
    return inner
@outer
def func():
    return '函数func'
print(func())