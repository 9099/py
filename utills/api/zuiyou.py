import requests
from Utils import fidder

head = '''
Host: tbapi.ixiaochuan.cn
Content-Length: 278
Content-Type: text/plain; charset=utf-8
Connection: Keep-Alive
Cookie: aliyungf_tc=AQAAAI6DGU10ZAoAyR9EMVz90Z/HBLC8
Cookie2: $Version=1
Accept-Encoding: gzip
ZYP: mid=34187505

'''
head=fidder.header2dict(head)
data = '{"offset":0,"filter":"video","tab":"rec","direction":"down","auto":0,"h_av":"3.6.4","h_dt":0,"h_os":22,"h_model":"m3 note","h_did":"862143030414424_a4:44:d1","h_nt":1,"h_m":34187505,"h_ch":"meizu","h_ts":1502671568783,"token":"TaK2NAplOdT3n8QV5PPjA3KEABE3dG8TbegonYfqFVDpXqYo="}'

res=requests.post('http://tbapi.ixiaochuan.cn/index/recommend?sign=6bf82b6962e7af7858cce3058c5d544e',data=data,headers=head)
print(res.json())