# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
import scrapy
import os
from scrapy.exceptions import  DropItem
from scrapy.pipelines.images import ImagesPipeline
import time
from Utils import fidder
import re
import requests
import pypinyin
import requests

class SunPipeline(object):
	def process_item(self, item, spider):
		conn = self.connect_mysql()
		cursor = conn.cursor()
		sql='insert into jiankangdemo(title) values(%s)'
		cursor.execute(sql,(item['title']))
		conn.commit()
		conn.close()

		return item
	def connect_mysql(self):
		conn = pymysql.connect(host="127.0.0.1",
							   port=3306,
							   user="root",
							   password="1234",
							   db="scrapy",
							   charset='utf8'


							   )
		return conn

class ToutiaoTechPipeline(object):
	def __init__(self):
		self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
		self.db = self.conn.toutiao
		self.coll = self.db.tech
	def process_item(self, item, spider):
		it=dict(item)

		try:
			self.coll.insert_one(it)
		except:
			return

		return item
class MamaQuanziPipeline(object):
	def __init__(self):
		pass
	def process_item(self, item, spider):
		if spider.name=='jb51':
			self.conn = pymongo.MongoClient(host='115.159.98.124', port=27017)
			self.db = self.conn.jb51
			self.coll = self.db.article
		if spider.name=='qinzi':
			self.conn = pymongo.MongoClient(host='115.159.98.124', port=27017)
			self.db = self.conn.qinzi
			self.coll = self.db.article1
		if spider.name=='gupiaozhishi':
			self.conn = pymongo.MongoClient(host='115.159.98.124', port=27017)
			self.db = self.conn.gupiao
			self.coll = self.db.zhishi
		it=dict(item)

		try:
			self.coll.insert_one(it)
		except:
			return

		return item

class MyImagePipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		for it in item['image_urls']:
			yield scrapy.Request(it)

	def item_completed(self, results, item, info):
		image_paths=[x['path'] for ok,x in results if ok]
		if not  image_paths:
			raise DropItem('No images')
		item['image_paths']=image_paths

		return item

	def file_path(self, request, response=None, info=None):
		return 'imgs/%s'%(request.url.split('/')[-1])

class UrlReplace(object):
	def __init__(self):
		pass

	def process_item(self, item, spider):

		urls=item['image_paths']
		global i
		i=0
		# try:
		def replace(img_url):
			global i
			imgurl=img_url.group()

			imgurl=urls[i]
			# assert isinstance(imgurl, str)
			i=i+1
			return 'src="'+imgurl+'"'

		import re
		item['content']=re.sub(r'src="(.+?)"',replace,item['content'])
		return item
		# except:
			# pass

class Demo(object):
	def process_item(self, item, spider):
		# item['demo']
		pass

def login_cookie(url, username, password):
		data = {'username': username,
		        'password': password,
		        'enews': 'login',
		        'equestion': '0',
		        'adminwindow': '0',
		        }
		from Utils import fidder
		head = '''
	Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://diguo1.com/e/admin/
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: application/x-www-form-urlencoded
	Accept-Encoding: gzip, deflate
	Content-Length: 185
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache

	'''.format(url)
		head = fidder.header2dict(head)
		tar = "http://www.{0}/e/admin/ecmsadmin.php".format(url)
		s = requests.post(tar, data=data, headers=head)

		d = ((s.cookies.get_dict()))
		s = ''
		for k, v in d.items():
			# k,v=i
			ss = k + '=' + v + ';'
			s += ss
		s = s[:-1]
		return s

def addclass(url, classname, bclassid=0, classpath=None, islast=1, cookie=None):
		classpath = ''.join(pypinyin.lazy_pinyin(classname))

		head = '''
		Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://{0}/e/admin/AddClass.php?enews=AddClass
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: application/x-www-form-urlencoded
	Accept-Encoding: gzip, deflate
	Content-Length: 1077
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {1}

		'''.format(url, cookie)
		data = 'enews=AddClass&classname={0}&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid={1}&ecmsclasstype=0&wburl=&oldwburl=&islast={3}&oldclasspath=&oldcpath=&pripath=collect%2F&classpath={2}&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=mmdd&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='.format(
			classname, bclassid, classpath, islast)
		# data='enews=AddClass&classname=1211&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid=60&ecmsclasstype=0&wburl=&oldwburl=&islast=1&oldclasspath=&oldcpath=&pripath=11111%2F&classpath=1211&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=Y-m-d&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='
		head = fidder.header2dict(head)
		url = 'http://{0}/e/admin/ecmsclass.php'.format(url)
		requests.post(url=url, data=data, headers=head)

def addcontent1(url, classid, title, content, cookie=None):
		# 	head='''
		# Accept: text/html, application/xhtml+xml, image/jxr, */*
		# Referer: http://diguo1.com/e/admin/AddNews.php?&enews=AddNews&classid={1}
		# Accept-Language: zh-CN
		# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
		# Content-Type: multipart/form-data; boundary=---------------------------7e1137a3021e
		# Accept-Encoding: gzip, deflate
		# Host: {0}
		# Connection: Keep-Alive
		# Pragma: no-cache
		# Cookie: {2}
		# 	'''.format(url,classid,cookie)
		head = '''
	Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://{0}/e/admin/AddNews.php?enews=AddNews&ecmsnfrom=1&bclassid=6&classid={1}
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: multipart/form-data; boundary=---------------------------7e1f9223021e
	Accept-Encoding: gzip, deflate
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {2}
		'''.format(url, classid, cookie)
		# print(head)

		data = '''
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="enews"

	AddNews
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="classid"

	{0}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="bclassid"

	5
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="id"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="filepass"

	1504323931
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="username"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldfilename"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldgroupid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldchecked"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstext_url"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmsfrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmsnfrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="fstb"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldttid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmscheck"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ztids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="zcids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldztids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldzcids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="havetmpic"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="title"

	{1}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titlecolor"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ftitle"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="checked"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="isgood"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="firsttitle"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="keyboard"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titleurl"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstime"

	2017-09-02 11:45:31
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titlepic"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="smalltext"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="writer"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="w_id"

	选择作者
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="befrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="befrom_id"

	选择信息来源
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstext"

	{2}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="dokey"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="qz_url"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="autosize"

	5000
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlepic"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlespicw"

	105
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlespich"

	118
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="istop"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstempid"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="groupid"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="userfen"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="onclick"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="totaldown"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newspath"

	2017-09-02
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="filename"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="infotags"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldinfotags"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_diyotherlink"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_keyid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_infouptime"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_infodowntime"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_title"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="v_vote_num"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="v_editnum"

	8
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_class"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="dovote_ip"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_olddotime"

	0000-00-00
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_dotime"

	0000-00-00
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_width"

	500
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_height"

	300
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_tempid"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="addnews"

	 提 交 
	-----------------------------7e1f9223021e--
	'''.format(classid, title, content)
		data = data.encode('utf-8')
		head = fidder.header2dict(head)
		url = 'http://{0}/e/admin/ecmsinfo.php'.format(url)
		s=requests.post(url=url, data=data, headers=head)
		print(s.content.decode('utf-8'))
def addcontent( url, classid, title, content, cookie=None):
	# 	head='''
	# Accept: text/html, application/xhtml+xml, image/jxr, */*
	# Referer: http://diguo1.com/e/admin/AddNews.php?&enews=AddNews&classid={1}
	# Accept-Language: zh-CN
	# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	# Content-Type: multipart/form-data; boundary=---------------------------7e1137a3021e
	# Accept-Encoding: gzip, deflate
	# Host: {0}
	# Connection: Keep-Alive
	# Pragma: no-cache
	# Cookie: {2}
	# 	'''.format(url,classid,cookie)
	head = '''
Accept: text/html, application/xhtml+xml, image/jxr, */*
Referer: http://{0}/e/admin/AddNews.php?enews=AddNews&ecmsnfrom=1&bclassid=6&classid={1}
Accept-Language: zh-CN
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
Content-Type: multipart/form-data; boundary=---------------------------7e1f9223021e
Accept-Encoding: gzip, deflate
Host: {0}
Connection: Keep-Alive
Pragma: no-cache
Cookie: {2}
	'''.format(url, classid, cookie)
	# print(head)

	data = '''
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="enews"

AddNews
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="classid"

{0}
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="bclassid"

5
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="id"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="filepass"

1504323931
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="username"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldfilename"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldgroupid"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldchecked"

1
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="newstext_url"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="ecmsfrom"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="ecmsnfrom"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="fstb"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldttid"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="ecmscheck"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="ztids"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="zcids"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldztids"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldzcids"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="havetmpic"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="title"

{1}
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="titlecolor"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="ftitle"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="checked"

1
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="isgood"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="firsttitle"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="keyboard"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="titleurl"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="newstime"

2017-09-02 11:45:31
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="titlepic"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="smalltext"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="writer"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="w_id"

选择作者
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="befrom"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="befrom_id"

选择信息来源
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="newstext"

{2}
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="dokey"

1
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="qz_url"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="autosize"

5000
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="getfirsttitlepic"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="getfirsttitlespicw"

105
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="getfirsttitlespich"

118
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="istop"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="newstempid"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="groupid"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="userfen"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="onclick"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="totaldown"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="newspath"

2017-09-02
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="filename"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="infotags"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="oldinfotags"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="info_diyotherlink"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="info_keyid"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="info_infouptime"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="info_infodowntime"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_title"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_name[]"


-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_num[]"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="v_vote_num"

1
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="v_editnum"

8
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_class"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="dovote_ip"

0
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_olddotime"

0000-00-00
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_dotime"

0000-00-00
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_width"

500
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_height"

300
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="vote_tempid"

1
-----------------------------7e1f9223021e
Content-Disposition: form-data; name="addnews"

 提 交 
-----------------------------7e1f9223021e--
'''.format(classid, title, content)
	data = data.encode('utf-8')
	head = fidder.header2dict(head)
	url = 'http://{0}/e/admin/ecmsinfo.php'.format(url)
	res=requests.post(url=url, data=data, headers=head)

	# if __name__ == '__main__':
	# 	cookie = login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
	# 	# print(cookie)
	# 	# addclass('igupiao.com.cn','cookie',islast=0,cookie=cookie)
	# 	addcontent('igupiao.com.cn', 12, 'demo', 'cookie', cookie=cookie)



class Diguo(object):
	cook=''
	def __init__(self,flag_first=True):
		print('==============================================')
		if flag_first:
			# Diguo.cook= login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
			# print(Diguo.cook)
			# self.addcontent('igupiao.com.cn', 13, 'dem111111o12', 'cookie11', cookie=Diguo.cook)
			# flag_first=False
			Diguo.cook = login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
			print(Diguo.cook+'========================获得Cookie======================')
			flag_first = False

		else:
			# print('2222==============================================')
			pass
		# coo = login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
		# print(coo+'-------------------------------------')

		# D()
	def process_item(self, item, spider):

		# self.addcontent('igupiao.com.cn',12,'demo','item[content]',cookie=Diguo.cook)
		addcontent('igupiao.com.cn', 2, item['title'], item['content'], cookie=Diguo.cook)
		print('===================添加内容====================')
		pass

	def login_cookie(self,url, username, password):
		data = {'username': username,
		        'password': password,
		        'enews': 'login',
		        'equestion': '0',
		        'adminwindow': '0',
		        }
		from Utils import fidder
		head = '''
	Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://diguo1.com/e/admin/
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: application/x-www-form-urlencoded
	Accept-Encoding: gzip, deflate
	Content-Length: 185
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache

	'''.format(url)
		head = fidder.header2dict(head)
		tar = "http://www.{0}/e/admin/ecmsadmin.php".format(url)
		s = requests.post(tar, data=data, headers=head)

		d = ((s.cookies.get_dict()))
		s = ''
		for k, v in d.items():
			# k,v=i
			ss = k + '=' + v + ';'
			s += ss
		s = s[:-1]
		return s

	def addclass(self,url, classname, bclassid=0, classpath=None, islast=1, cookie=None):
		classpath = ''.join(pypinyin.lazy_pinyin(classname))

		head = '''
		Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://{0}/e/admin/AddClass.php?enews=AddClass
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: application/x-www-form-urlencoded
	Accept-Encoding: gzip, deflate
	Content-Length: 1077
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {1}

		'''.format(url, cookie)
		data = 'enews=AddClass&classname={0}&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid={1}&ecmsclasstype=0&wburl=&oldwburl=&islast={3}&oldclasspath=&oldcpath=&pripath=collect%2F&classpath={2}&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=mmdd&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='.format(
			classname, bclassid, classpath, islast)
		# data='enews=AddClass&classname=1211&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid=60&ecmsclasstype=0&wburl=&oldwburl=&islast=1&oldclasspath=&oldcpath=&pripath=11111%2F&classpath=1211&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=Y-m-d&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='
		head = fidder.header2dict(head)
		url = 'http://{0}/e/admin/ecmsclass.php'.format(url)
		requests.post(url=url, data=data, headers=head)

	def addcontent(self,url, classid, title, content, cookie=None):
		# 	head='''
		# Accept: text/html, application/xhtml+xml, image/jxr, */*
		# Referer: http://diguo1.com/e/admin/AddNews.php?&enews=AddNews&classid={1}
		# Accept-Language: zh-CN
		# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
		# Content-Type: multipart/form-data; boundary=---------------------------7e1137a3021e
		# Accept-Encoding: gzip, deflate
		# Host: {0}
		# Connection: Keep-Alive
		# Pragma: no-cache
		# Cookie: {2}
		# 	'''.format(url,classid,cookie)
		head = '''
	Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://{0}/e/admin/AddNews.php?enews=AddNews&ecmsnfrom=1&bclassid=6&classid={1}
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: multipart/form-data; boundary=---------------------------7e1f9223021e
	Accept-Encoding: gzip, deflate
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {2}
		'''.format(url, classid, cookie)
		# print(head)

		data = '''
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="enews"

	AddNews
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="classid"

	{0}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="bclassid"

	5
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="id"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="filepass"

	1504323931
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="username"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldfilename"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldgroupid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldchecked"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstext_url"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmsfrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmsnfrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="fstb"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldttid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ecmscheck"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ztids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="zcids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldztids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldzcids"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="havetmpic"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="title"

	{1}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titlecolor"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="ftitle"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="checked"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="isgood"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="firsttitle"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="keyboard"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titleurl"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstime"

	2017-09-02 11:45:31
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="titlepic"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="smalltext"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="writer"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="w_id"

	选择作者
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="befrom"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="befrom_id"

	选择信息来源
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstext"

	{2}
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="dokey"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="qz_url"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="autosize"

	5000
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlepic"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlespicw"

	105
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="getfirsttitlespich"

	118
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="istop"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newstempid"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="groupid"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="userfen"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="onclick"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="totaldown"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="newspath"

	2017-09-02
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="filename"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="infotags"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="oldinfotags"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_diyotherlink"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_keyid"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_infouptime"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="info_infodowntime"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_title"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="v_vote_num"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="v_editnum"

	8
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_class"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="dovote_ip"

	0
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_olddotime"

	0000-00-00
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_dotime"

	0000-00-00
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_width"

	500
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_height"

	300
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="vote_tempid"

	1
	-----------------------------7e1f9223021e
	Content-Disposition: form-data; name="addnews"

	 提 交 
	-----------------------------7e1f9223021e--
	'''.format(classid, title, content)
		data = data.encode('utf-8')
		head = fidder.header2dict(head)
		url = 'http://{0}/e/admin/ecmsinfo.php'.format(url)
		requests.post(url=url, data=data, headers=head)

	# if __name__ == '__main__':
	# 	cookie = login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
	# 	# print(cookie)
	# 	# addclass('igupiao.com.cn','cookie',islast=0,cookie=cookie)
	# 	addcontent('igupiao.com.cn', 12, 'demo', 'cookie', cookie=cookie)