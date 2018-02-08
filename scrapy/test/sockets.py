#coding=utf-8
#使用socket模块编写的服务器（通过UDP传输数据）
import socket

import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9090)) #bind函数只有一个参数
s.send(b'nisidhisd')
time.sleep(2)
s.send(b'exit')
while True:
	data=s.recv(1024)
	if data:
		print(data)
s.close()
# while True:
# 	# data,client=s.recvfrom(1024)
# 	# print ("receive a connection from %s"  %str(client))   #str（）函数可以将元组转换成字符串形式
# # #回显
# 	# s.sendto("echo:"+data,client)
# 	d=s.recv(1024)
# 	if d:
# 		data.append(d)
# 	else:
# 		break
# # data = ''.join(data.extend('utf-8'))
# print(data)

