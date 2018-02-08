#coding:utf-8
from lxml import html
from optparse import OptionParser
s='''
<?xml version="1.0" encoding="ISO-8859-1"?>
<catalog>
　<cd country="USA">
　　<title>Empire Burlesque</title>
　　<artist>Bob Dylan</artist>
　　<price>10.90</price>
　</cd>
　<cd country="UK">
　　<title>Hide your heart</title>
　　<artist>Bonnie Tyler</artist>
　　<price>9.90</price>
　</cd>
　<cd country="USA">
　　<title>Greatest Hits</title>
　　<artist>Dolly Parton</artist>
　　<price>9.90
<a>9</a>
</price>
　</cd>
</catalog>
'''
x=html.document_fromstring(s)
res=x.xpath('//cd/descendant::node()[contains(text(),"9")]/text()')
print(res)