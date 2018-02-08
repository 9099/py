#encoding : utf-8
# import  subprocess
# s =subprocess.Popen(['ipconfig'],stdout=subprocess.PIPE)
#
# ss=s.communicate()
# for i in ss:
# 	print(i.decode('gb2312',errors='ignore'))
# from scapy.all import ARP

def dec(func):
	def inner():
		print('I am :function',func.__name__)

		return func
	return inner
@dec
def fun():
	print('i am you')

if __name__ == '__main__':
	print(fun)
from keras.layers import core