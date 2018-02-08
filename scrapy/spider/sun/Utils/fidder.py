import random
import json
import requests
import time

def taobao2mp4(url):
	url=url[:-3]+'mp4'
	url=url.split('/')
	url.pop(-2)
	url.pop(-2)
	url[-4]='6'
	url='/'.join(url)
	return url

def header2dict(header):
	header = header.strip().split('\n')
	buff=[]
	for i in header:
		buff.append(i.strip())
	buff = {x.split(':', maxsplit=1)[0]: x.split(':', maxsplit=1)[1].strip() for x in buff}
	return buff

def post2dict(data):
	data = data.split('&')
	data = {x.split('=')[0]: x.split('=')[1] for x in data}
	return data

def domain_ename(domain):
	domain=str(domain).lower()
	head = '''
Host: www.ename.net
Connection: keep-alive
Content-Length: 79
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.ename.net
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.ename.net/domain?domain=ww&ext%5B%5D=.com&ext%5B%5D=.net&ext%5B%5D=.cn&ext%5B%5D=.com.cn&ext%5B%5D=.wang&ext%5B%5D=.club&ext%5B%5D=.cc
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: ext=.com%2C.net%2C.cn%2C.com.cn%2C.cc%2C.wang%2C.club%2C; PHPSESSID=6pueqpki48amfjc489fu9ptu57; __guid=58027948.4394530496357793000.1502531818698.5598; UM_distinctid=15dd5e017acd5-08dd6dd98e9a19-5d4e211f-100200-15dd5e017ad215; UserClientIcon=ad597d69c52a94bb7d4f878b1c067b5d; emanage_csrf_cookie_name=6e28974299ff14f32378dc0d1458b08c; monitor_count=4; CNZZDATA1252919809=561056888-1502527717-http%253A%252F%252Fwww.dnbbs.com%252F%7C1502530162
	'''
	head = header2dict(head)
	d = post2dict('choseType=1&domain=ww.wang&key=706b478ff756bda4e89e7508d7fde745&time=1502531982')
	d['domain']=domain
	# d['time'] = int(time.time())-random.randint(20,400)
	# print(d)
	rea = requests.post('https://www.ename.net/domain/domainAjax',data=d,headers=head)
	res=rea.json()
	# print(res)
	flag=res['result'][domain]['code']
	if flag==1:
		return False
	elif flag==0:
		return True
	else:
		return 'Error'

def whios_baidu(domain):
	head='''
Host: cloud.baidu.com
Connection: keep-alive
Content-Length: 36
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://cloud.baidu.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/json
Referer: https://cloud.baidu.com/product/bcd/whois.html?domain=sdj.com
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: BAIDUID=B21220053BEC42415C54C4B6A580EB03:FG=1; BDUSS=hNLTRUTUg0bjlSenExLXNnfk45NTlSOTQ2WnpQMzB4LWJ2TzRCeEo2bGpBTEZaTUFBQUFBJCQAAAAAAAAAAAEAAACN6jQ3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGNziVljc4lZS1; BIDUPSID=B21220053BEC42415C54C4B6A580EB03; PSTM=1502180312; cflag=15%3A3; __guid=233031500.4139926570336259600.1503136113006.1104; monitor_count=11; Hm_lvt_28a17f66627d87f1d046eae152a1c93d=1503136117; Hm_lpvt_28a17f66627d87f1d046eae152a1c93d=1503136612

'''
	head=header2dict(head)
	js=(r'{"domain":"%s","type":"NORMAL"}'%(domain))
	js=eval(js)
	res=requests.post('http://cloud.baidu.com/api/bcd/whois/detail',json=js,headers=head)
	return res.json()

def domain_xin(prefix,suffix):
	head='''
	Host: checkdomain.xinnet.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Accept: */*
Referer: http://www.xinnet.com/domain/domain_search_result_version2.jsp?prefix=dfege&suffix=.com&domainSuffixType=null
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: uid=42068A57073D41358ADBE696CA81F2A9; sId=58674BB8394A436E881FCD3ABDF0E93C; xinnet_id=6c6fa53dcf045243da7b8e07896c95ea; _gat=1; _ga=GA1.2.1846579234.1503359294; _gid=GA1.2.276100885.1503359294; _page=http%3A%2F%2Fwww.xinnet.com%2Fdomain%2Fdomain.html%3Futm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_term%3D%25E7%259F%25AD%25E5%259F%259F%25E5%2590%258D%26utm_content%3D%25E5%259F%259F%25E5%2590%258D%25E7%25B1%25BB-%25E5%259F%259F%25E5%2590%258D%26utm_campaign%3Dpc-%25E5%259F%259F%25E5%2590%258D%25E7%25B1%25BB-%25E9%2595%25BF%25E5%25B0%25BE%25E8%25AF%258D; frontUrl=http%3A%2F%2Fwww.xinnet.com%2Fdomain%2Fdomain_search_result_version2.jsp%3Fprefix%3Ddfege%26suffix%3D.com%26domainSuffixType%3Dnull; pageno=2

'''
	head=header2dict(head)
	url='http://checkdomain.xinnet.com/domainCheck?callbackparam=jQuery172005179644904652658_1503359299461&searchRandom=9&prefix={0}&suffix=.{1}&_=1503359350313'.format(prefix,suffix)
	res= str(requests.get(url,headers=head).content)
	start=res.index('(')
	res=res[start+1:-2]
	return res
if __name__=='__main__':
	# s=requests.session()
	js={"offset":0,"filter":"all","tab":"rec","direction":"down","auto":0,"h_av":"3.6.4","h_dt":0,"h_os":22,"h_model":"m3 note","h_did":"862143030414424_a4:44:d1","h_nt":1,"h_m":34187505,"h_ch":"meizu","h_ts":1502499919077,"token":"T0K7NAplOdT3n8QV5PPjA3KEABGswfStfZgxtvA7kigBGGjs="}
	# js=json.loads(js)
	head='''
	Host: www.ename.net
Connection: keep-alive
Content-Length: 79
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.ename.net
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.ename.net/domain?domain=ww&ext%5B%5D=.com&ext%5B%5D=.net&ext%5B%5D=.cn&ext%5B%5D=.com.cn&ext%5B%5D=.wang&ext%5B%5D=.club&ext%5B%5D=.cc
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: ext=.com%2C.net%2C.cn%2C.com.cn%2C.cc%2C.wang%2C.club%2C; PHPSESSID=6pueqpki48amfjc489fu9ptu57; __guid=58027948.4394530496357793000.1502531818698.5598; UM_distinctid=15dd5e017acd5-08dd6dd98e9a19-5d4e211f-100200-15dd5e017ad215; UserClientIcon=ad597d69c52a94bb7d4f878b1c067b5d; emanage_csrf_cookie_name=6e28974299ff14f32378dc0d1458b08c; monitor_count=4; CNZZDATA1252919809=561056888-1502527717-http%253A%252F%252Fwww.dnbbs.com%252F%7C1502530162


	'''

	# cook={'Cookie':'aliyungf_tc=AQAAANmyNyZBUAIAWxxEMTqweX5qmG2E','Cookie2':'$Version=1'}
	# head=header2dict(head)
	# s.cookies=cook
	# print(head)
	#
	# s.headers=head
	# print(head)
	# data=post2dict('choseType=1&domain=ww.wang&key=706b478ff756bda4e89e7508d7fde745&time=1502531982')
	# print(data)
	# rea = requests.post('https://www.ename.net/domain/domainAjax',headers=head,data=data)
	# print(rea.content)
	# print(taobao2mp4('http://cloud.video.taobao.com/play/u/2821843773/p/1/e/1/t/1/fv/102/39521798.swf'))
	# alph='abcdefghijklmnopqrstuvwxyz'
	# sufix=['.com','.cn','.com.cn','.net','.org','.cc']

	# for i in range(999):
	# 	s = ''.join(random.sample(alph, int(random.choice('4'))))
	# 	for ii in range(6):
	# 		dom=s+sufix[ii]
	# 		res=domain_ename(dom)
	# 		if res==True:
	# 			print(dom)
	# 		else:
	# 			pass
	# print(domain_ename('moocx.com'))
	print(domain_xin("baidua","cn"))
