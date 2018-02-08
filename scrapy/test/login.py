import requests


def login_cookie(url,username,password):
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



cookie=login_cookie('igupiao.com.cn','admin','Mnbvcx1!')