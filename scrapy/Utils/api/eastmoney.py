from Utils import fidder
import requests

head = '''
	Content-Type: application/x-www-form-urlencoded
	Content-Length: 142
	Host: gubaapi.eastmoney.com
	Connection: Keep-Alive
	Accept-Encoding: gzip
	User-Agent: okhttp/3.3.1

'''
head=fidder.header2dict(head)
data='p=1&pi=&sorttype=1&ps=20&version=6009006&ctoken=&plat=Android&deviceid=0d74d7c048f912d142dbe94ec1570765&utoken=&code=SZ002600&product=StockWay'
data=fidder.post2dict(data)
res=requests.post('http://gubaapi.eastmoney.com/v3/read/Custom/Mobie/ArticleList.aspx',data=data,headers=head)

s=str(res.json())
s=s.replace("'",'"')
s=s.replace('False','"False"')
print(s)