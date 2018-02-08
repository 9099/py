# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from sun.items import Jb51
# from scrapy.

class Jb51Spider(CrawlSpider):
	name = 'jb51'
	allowed_domains = ['jb51.net']
	start_urls = ['http://www.jb51.net/cms/list408_1.html',
	              'http://www.jb51.net/cms/list586_1.html',
				  'http://www.jb51.net/cms/list418_1.html',
				  'http://www.jb51.net/cms/list417_1.html',
				  'http://www.jb51.net/cms/list416_1.html',
				  'http://www.jb51.net/cms/list415_1.html',
				  'http://www.jb51.net/cms/list414_1.html',
				  'http://www.jb51.net/cms/list413_1.html',
				  'http://www.jb51.net/cms/list412_1.html',
				  'http://www.jb51.net/cms/list409_1.html',
				  'http://www.jb51.net/cms/list411_1.html',
				  'http://www.jb51.net/cms/list578_1.html',
				  'http://www.jb51.net/cms/list419_1.html',
				  'http://www.jb51.net/cms/list475_1.html',
				  ]
	rules =[
		Rule(LinkExtractor(restrict_xpaths=('//div[@class="dxypage clearfix"]/a[contains(text(),"下")]'))),
		Rule(LinkExtractor(allow=(r'http://www.jb51.net/.+/.+'),
		                   restrict_xpaths=('//div[@class="artlistBar border"]')), callback='parse_item'),


	 ]
	def next_list(self,response):
		url=response.xpath('//div[@class="dxypage clearfix"]/a[last()-1]/@href').extract()[0]
		if url:
			url=urljoin(response.url,url)
			return scrapy.Request(url=url,callback=self.parse)
	# def parse_list(self, response):
	# 	return scrapy.Request()
	def parse_item(self, response):
		title=response.xpath('//h1/text()').extract()[0]
		summary=response.xpath('//div[@class="art_desc mt10"]').extract()[0]
		cont=response.xpath('//div[@id="content"]').extract()[0]
		# label=response.xpath('//div[@class="box mb15 mt10"]/node()')[-4:-1:2].xpath('string(.)').extract()
		label=response.xpath('//div[@class="box mb15 mt10"]/node()')[3:].xpath('string(.)').extract()
		data=Jb51()
		d={}
		d['title']=title
		d['summary']=summary
		d['content']=cont
		d['label']=label
		data=d
		yield data
