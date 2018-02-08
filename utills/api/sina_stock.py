#encoding:utf-8
import requests
import time
stoc=''
url = 'http://hq.sinajs.cn/list=sh601006'
stock = requests.get(url)
stock=str(stock.content)
info = (stock.split('"')[1])
info=info.split(',')
for i in info:
	print(i)