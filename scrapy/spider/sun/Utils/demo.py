import time
import random

from lxml import html
import requests
# s=requests.get('http://www.cxw.com/whois?domain=sdef.com')
# doc=html.parse('http://www.cxw.com/whois?domain=sdef.com')

# con=doc.xpath('//div[@class="tableWhoisTd"]/span/text()')
# con1=doc.xpath('//tbody/tr[1]/td[2]/text()')
# for i in con:
# 	print(i)
import m3u8

s=m3u8.load(r'C:\Users\Administrator\Desktop\scrapy\test\m3u81')

def loadM3u8(m3u8url):
    def load_m3u8(url):
        urls = []
        m = m3u8.load(url)
        for seg in m.segments:
            urls.append(seg.absolute_uri)
        return urls
    try:
        videoUrls = load_m3u8(m3u8url)
    except Exception as e:
        # print('load_m3u8 {}'.format(e))
        return {'reason': 'load_m3u8 {}'.format(e)}
    else:
        return {'videoUrls': videoUrls}
print(loadM3u8(r'C:\Users\Administrator\Desktop\scrapy\test\m3u81'))
