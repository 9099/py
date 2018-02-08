# # -*- coding: utf-8 -*-
# # author: orangleliu date: 2014-11-12
# # python2.7.x ip_scaner.py
#
# '''''
# 不同平台，实现对所在内网端的ip扫描
#
# 有时候需要知道所在局域网的有效ip，但是又不想找特定的工具来扫描。
# 使用方法 python ip_scaner.py 192.168.1.1
# (会扫描192.168.1.1-255的ip)
# '''
#
# import platform
# import sys
# import os
# import time
# import threading
#
#
# def get_os():
# 	'''''
# 	get os 类型
# 	'''
# 	os = platform.system()
# 	print('os',os)
# 	if os == "Windows":
# 		return "n"
# 	else:
# 		return "c"
#
#
# def ping_ip(ip_str):
# 	cmd = ["ping", "-{op}".format(op=get_os()),
# 	       "1", ip_str]
# 	output = os.popen(" ".join(cmd)).readlines()
#
# 	flag = False
# 	for line in list(output):
# 		if not line:
# 			continue
# 		if str(line).upper().find("TTL") >= 0:
# 			flag = True
# 			break
# 	if flag:
# 		print("ip: %s is ok ***" % ip_str)
#
#
# def find_ip(ip_prefix):
# 	'''''
# 	给出当前的127.0.0 ，然后扫描整个段所有地址
# 	'''
# 	for i in range(1, 256):
# 		ip = '%s.%s' % (ip_prefix, i)
# 		threading.Thread(ping_ip, (ip,))
# 		time.sleep(0.3)
#
#
# if __name__ == "__main__":
# 	print("start time %s" % time.ctime())
# 	# commandargs = sys.argv[1:]
# 	# args = "".join(commandargs)
#
# 	# ip_prefix = '.'.join(args.split('.')[:-1])
# 	# find_ip('192.168.1')
# 	get_os()
# 	print("end time %s" % time.ctime())

#
# import re
#
# import requests
# import urllib3.request
# url = 'http://admin:netcenter@192.168.1.1/analyze.cgi?page=1&px=3&sf=1'
# a = requests.get(url).content
# ip = re.findall(r'192\.168\.\d+\.\d+', a, re.M)
# ip1 = ip[0]
# ip2 = ip[1]
# ip3 = ip[2]
# print ("当前消耗网络带宽最大的前三个ip是"+ip1+" "+ip2+" "+ip3)


from scapy.all import srp,Ether,ARP,conf
ipscan='192.168.1.1/24'
try:
	ans,unans = srp(Ether(dst=b"FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan),timeout=2,verbose=False)



except Exception as e:
	print ((e))
else:
	for snd,rcv in ans:
		list_mac=rcv.sprintf("%Ether.src% - %ARP.psrc%")
		print (list_mac)



import subprocess
sub=subprocess.Popen(subprocess.PIPE)
sub.communicate()
