#!/usr/bin/python
#encoding:utf-8
import subprocess
import shlex
import dpkt
from idna import unicode
# arg=input('input\n')
# arg=shlex.split(arg)
# # print(arg)
# p = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
#
# p.wait()
f = open('demo.cap', 'rb')
pcap = dpkt.pcap.Reader(f)

# for ts, buf in pcap:
# 	eth = dpkt.ethernet.Ethernet(buf)
# 	# print(buf)
# 	ip = eth.data
# 	tcp = ip.data
# 	# print(ip,tcp)
# 	try:
# 		if len(tcp.data) > 0:
# 			http = dpkt.http.Request(tcp.data)
# 			if http :
# 				print(http.headers['host'] + http.uri + '\n' + http.body,)  # ,http.headers['user-agent']
# 				print('\n\n')
# 	except:
# 		pass

for ts,buffer in pcap:
	eth=dpkt.ethernet.Ethernet(buffer)
	ip=eth.data
	tcp=ip.data
	if tcp.dport==80 and len(tcp.data):
		http=dpkt.http.Request(tcp.data)
		print(http.headers)

f.close()


# GET /p.php?act=rt&callback=jQuery170207851311353634_1503128145602&_=1503128148740 HTTP/1.1
# host: 115.159.98.124
# connection: keep-alive
# accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01
# x-requested-with: XMLHttpRequest
# user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
# referer: http://115.159.98.124/p.php
# accept-encoding: gzip, deflate
# accept-language: zh-CN,zh;q=0.8
