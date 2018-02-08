import requests
import socket
from lxml import html
def kuaidaili(num):
	res=requests.get('http://www.kuaidaili.com/free/inha/{}/'.format(num)).content
	res=html.document_fromstring(res)
	ip=res.xpath('//tr/td[1]/text()')
	port=res.xpath('//tr/td[2]/text()')
	return dict(zip(ip,port))
if __name__=='__main__':
	# di={'180.111.154.232':'8118'}
	for s in range(300):
		di=kuaidaili(s)
		ip=list(di.keys())
		port=list(di.values())
		for i in range(len(port)):
			ip_addr=ip[i]
			porter=port[i]
			pro=ip_addr+':'+porter

			p={'https':'{}'.format(pro),'http':'{}'.format(pro)}

			try:
				for ii in range(3):
					s=requests.get('http://115.159.98.124/ip.php',proxies=p,timeout=4)
					if ip_addr == (s.content.decode('utf-8')):
						# print(ip_addr)
						with open('proxies.csv','a+') as f:
							f.write(ip_addr+','+porter+'\n')
						break
					else:
						pass
			except:
				pass
