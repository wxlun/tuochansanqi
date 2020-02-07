import socket
import select

###############HTTP请求的本质，阻塞######################################
"""
sk = socket.socket()
#1.连接
sk.connect(('www.baidu.com',80,)) #IO阻塞
print('连接成功了...')

#2.连接成功发送消息
sk.send(b'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\nk1=v1&k2=v2')

#3.等待着服务端响应
data = sk.recv(8096) #IO阻塞
print(data)

#关闭连接
sk.close()
"""



###############HTTP请求的本质，非阻塞######################################
