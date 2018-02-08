import requests

from lxml.html import parse
# start_url='http://top.chinaz.com/hangye/index_yiliao.html'
# html=parse(start_url)
# name=html.xpath('//h3[@class="rightTxtHead"]/a/text()')
# url=html.xpath('//h3[@class="rightTxtHead"]/span/text()')
# l=len(url)-10
urls = ['39.net']

for i in urls:
	# name_=name[i]
	# url_=url[i]
	# print(name,url)
	res=parse('http://www.'+i)
	title=''.join(res.xpath('//head//title/text()'))
	# print(title)
	key=''.join(res.xpath('//head//meta[@name="keywords"]/@content'))
	des=''.join(res.xpath('//head//meta[@name="description"]/@content'))
	print('-----------------------------------------')
	print('----->>>>'+i)
	print('title--->>'+title)
	print('keyword--->>'+key)
	print('description--->>'+des)
	print('-----------------------------------------')
print(i)