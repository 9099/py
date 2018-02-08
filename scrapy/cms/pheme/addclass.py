#coding:utf-8
from Utils import fidder
import re
import requests
import time
import pypinyin
import requests

class demo:
	# def __init__(self):
	# 	pass
	def login_cookie(self,url,username,password):
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
		tar="http://www.{0}/e/admin/ecmsadmin.php".format(url)
		s = requests.post(tar, data=data, headers=head, allow_redirects=True)

		d = ((s.cookies.get_dict()))
		s = ''
		for k, v in d.items():
			# k,v=i
			ss = k + '=' + v + ';'
			s += ss
		s = s[:-1]
		return s

	def addclass(self,url,classname,bclassid=0,classpath=None,islast=1,cookie=None):
		classpath=''.join(pypinyin.lazy_pinyin(classname))

		head='''
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
	
		'''.format(url,cookie)
		data='enews=AddClass&classname={0}&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid={1}&ecmsclasstype=0&wburl=&oldwburl=&islast={3}&oldclasspath=&oldcpath=&pripath=collect%2F&classpath={2}&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=mmdd&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='.format(classname,bclassid,classpath,islast)
		# data='enews=AddClass&classname=1211&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid=60&ecmsclasstype=0&wburl=&oldwburl=&islast=1&oldclasspath=&oldcpath=&pripath=11111%2F&classpath=1211&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=Y-m-d&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='
		head=fidder.header2dict(head)
		url='http://{0}/e/admin/ecmsclass.php'.format(url)
		requests.post(url=url,data=data,headers=head)

	def addcontent(self,url,classid,title,content,cookie=None):
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
		head='''
	Accept: text/html, application/xhtml+xml, image/jxr, */*
	Referer: http://{0}/e/admin/AddNews.php?&enews=AddNews&classid={1}
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: multipart/form-data; boundary=---------------------------7e13dc312039c
	Accept-Encoding: gzip, deflate
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {2}
		'''.format(url,classid,cookie)
		# print(head)

		data='''
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="enews"
	
	AddNews
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="classid"
	
	{0}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="bclassid"
	
	5
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="id"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="filepass"
	
	1504323931
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="username"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldfilename"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldgroupid"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldchecked"
	
	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstext_url"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmsfrom"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmsnfrom"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="fstb"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldttid"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmscheck"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ztids"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="zcids"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldztids"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldzcids"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="havetmpic"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="title"
	
	{1}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titlecolor"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ftitle"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="checked"
	
	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="isgood"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="firsttitle"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="keyboard"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titleurl"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstime"
	
	2017-09-02 11:45:31
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titlepic"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="smalltext"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="writer"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="w_id"
	
	选择作者
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="befrom"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="befrom_id"
	
	选择信息来源
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstext"
	
	{2}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="dokey"
	
	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="qz_url"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="autosize"
	
	5000
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlepic"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlespicw"
	
	105
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlespich"
	
	118
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="istop"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstempid"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="groupid"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="userfen"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="onclick"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="totaldown"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newspath"
	
	2017-09-02
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="filename"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="infotags"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldinfotags"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_diyotherlink"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_keyid"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_infouptime"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_infodowntime"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_title"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"
	
	
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="v_vote_num"
	
	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="v_editnum"
	
	8
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_class"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="dovote_ip"
	
	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_olddotime"
	
	0000-00-00
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_dotime"
	
	0000-00-00
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_width"
	
	500
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_height"
	
	300
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_tempid"
	
	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="addnews"
	
	 提 交 
	-----------------------------7e13dc312039c--
	'''.format(classid,title,content)
		data=data.encode('utf-8')
		head=fidder.header2dict(head)
		url='http://{0}/e/admin/ecmsinfo.php'.format(url)
		requests.post(url=url,data=data,headers=head)
		print('+++++++++++++++')

def login_cookie( url, username, password):
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
		s = requests.post(tar, data=data, headers=head, allow_redirects=True)

		d = ((s.cookies.get_dict()))
		s = ''
		for k, v in d.items():
			# k,v=i
			ss = k + '=' + v + ';'
			s += ss
		s = s[:-1]
		return s

def addclass( url, classname, bclassid=0, classpath=None, islast=1, cookie=None):
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
			classname, bclassid, classpath, islast).encode('utf-8')
		# data='enews=AddClass&classname=1211&oldbclassid=&classid=0&oldclassname=&oldislast=&filepass=&bname=&bclassid=60&ecmsclasstype=0&wburl=&oldwburl=&islast=1&oldclasspath=&oldcpath=&pripath=11111%2F&classpath=1211&modid=1&oldmodid=&yhid=%E4%B8%8D%E4%BD%BF%E7%94%A8&classurl=&classimg=&classpagekey=&intro=&showclass=0&myorder=0&openadd=1&oldopenadd=&qaddlist=0&checkqadd=0&addinfofen=0&adminqinfo=0&addreinfo=1&haddlist=0&checked=1&wfid=0&definfovoteid=0&groupid=0&openpl=0&doctime=0&down_num=2&online_num=2&smallbdinfoid=&islist=0&oldislist=&bdinfoid=&classtempid=1&listtempid=1&dtlisttempid=1&newstempid=1&pltempid=0&searchtempid=0&wapstyleid=0&classtext=&listdt=0&oldlistdt=&showdt=0&listorder=id+DESC&lorderselect=id+DESC&reorder=newstime+DESC&orderselect=newstime+DESC&classtype=.html&select=.html&oldclasstype=.html&maxnum=0&repagenum=&lencord=25&oldlencord=25&link_num=10&infopath=0&ipath=&newspath=Y-m-d&select2=Y-m-d&filename_qz=&filename=0&filetype=.html&select3=.html&keycid=0&jstempid=1&newline=10&hotline=10&goodline=10&hotplline=10&firstline=10&Submit=%E6%8F%90%E4%BA%A4&from='
		head = fidder.header2dict(head)
		url = 'http://{0}/e/admin/ecmsclass.php'.format(url)
		requests.post(url=url, data=data, headers=head)

def addcontent(url,classid, title, content, cookie=None):
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
	Referer: http://{0}/e/admin/AddNews.php?&enews=AddNews&classid={1}
	Accept-Language: zh-CN
	User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	Content-Type: multipart/form-data; boundary=---------------------------7e13dc312039c
	Accept-Encoding: gzip, deflate
	Host: {0}
	Connection: Keep-Alive
	Pragma: no-cache
	Cookie: {2}
		'''.format(url, classid, cookie)
		# print(head)

		data = '''
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="enews"

	AddNews
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="classid"

	{0}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="bclassid"

	5
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="id"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="filepass"

	1504323931
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="username"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldfilename"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldgroupid"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldchecked"

	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstext_url"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmsfrom"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmsnfrom"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="fstb"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldttid"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ecmscheck"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ztids"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="zcids"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldztids"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldzcids"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="havetmpic"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="title"

	{1}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titlecolor"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="ftitle"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="checked"

	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="isgood"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="firsttitle"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="keyboard"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titleurl"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstime"

	2017-09-02 11:45:31
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="titlepic"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="smalltext"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="writer"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="w_id"

	选择作者
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="befrom"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="befrom_id"

	选择信息来源
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstext"

	{2}
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="dokey"

	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="qz_url"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="autosize"

	5000
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlepic"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlespicw"

	105
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="getfirsttitlespich"

	118
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="istop"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newstempid"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="groupid"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="userfen"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="onclick"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="totaldown"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="newspath"

	2017-09-02
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="filename"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="infotags"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="oldinfotags"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_diyotherlink"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_keyid"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_infouptime"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="info_infodowntime"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_title"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_name[]"


	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_num[]"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="v_vote_num"

	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="v_editnum"

	8
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_class"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="dovote_ip"

	0
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_olddotime"

	0000-00-00
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_dotime"

	0000-00-00
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_width"

	500
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_height"

	300
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="vote_tempid"

	1
	-----------------------------7e13dc312039c
	Content-Disposition: form-data; name="addnews"

	 提 交 
	-----------------------------7e13dc312039c--
	'''.format(classid, title, content)
		data = data.encode('utf-8')
		head = fidder.header2dict(head)
		urll = 'http://{0}/e/admin/ecmsinfo.php'.format(url)
		# urll = 'http://www.i/gupiao.com.cn/e/admin/AddNews.php?enews=AddNews&ecmsnfrom=1&bclassid=6&classid=12'
		# data1='enews=AddNews&classid=[分类ID]&bclassid=6&id=0&username=&oldfilename=&oldgroupid=&oldchecked=1&newstext_url=&ecmsnfrom=1&fstb=&oldttid=&ecmscheck=0&ztids=&zcids=&oldztids=&oldzcids=&havetmpic=0&title=[标签:标题]&titlecolor=&ftitle=&checked=1&isgood=0&firsttitle=0&keyboard=&titleurl=&newstime=[系统时间转化:yyyy-MM-dd]&titlepic=&smalltext=&writer=&w_id=选择作者&befrom=&befrom_id=选择信息来源&dokey=1&qz_url=&autosize=5000&getfirsttitlepic=&getfirsttitlespicw=105&getfirsttitlespich=118&istop=0&newstempid=0&groupid=0&userfen=0&onclick=0&totaldown=0&newspath=&filename=&infotags=&oldinfotags=&info_diyotherlink=0&info_keyid=&info_infouptime=&info_infodowntime=&vote_title=&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&vote_name[]=&vote_num[]=0&v_vote_num=1&v_editnum=8&vote_class=0&dovote_ip=0&vote_olddotime=0000-00-00&vote_dotime=0000-00-00&vote_width=500&vote_height=300&vote_tempid=1&addnews=提 交&newstext=[标签:内容]'.encode('utf-8')
		# data1={
		# 	'enews':'AddNew',
		# 	'classid':'13',
		# 	'bclassid':'6',
		# 	'ecmsnfrom':'1',
		# 	'title':'aaaaaa',
		# 	'newstext':'asads',
		# }
		s=requests.post(url=urll, data=data, headers=head)
		print(s.content.decode('utf-8'))
if __name__=='__main__':
	# a=demo()
	# cook = a.login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
	# print(cookie)
	# addclass('igupiao.com.cn','cookie',islast=0,cookie=cook)
	# a.addcontent(url='igupiao.com.cn',classid=12,title='demo',content='cookie11',cookie=cook)

	# coo=login_cookie('igupiao.com.cn', 'admin', 'Mnbvcx1!')
	coo=login_cookie('52baobei.cn', 'admin', 'Mnbvcx1!')
	# print(coo)
	# 基础知识交易指南政策法规股票术语基本知识
	cont = ['孕前准备','生男生女','遗传优生','孕前饮食']
	for i in cont:
		# print(i)
		addclass('52baobei.cn', i, islast=1, cookie=coo)
	# addcontent('igupiao.com.cn', 13, 'demo12', 'cookie11', cookie=coo)
	# s=requests.post('http://www.igupiao.com.cn/e/admin/AddNews.php?enews=AddNews&ecmsnfrom=1&bclassid=6&classid=12',cookies=coo)
	# print(s.headers)

	# print(pypinyin.lazy_pinyin('你哈'))
