# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sun.items import MamaBaike
# from scrapy.pipelines.images import ImagesPipeline

class MamaSpider(CrawlSpider):
	name = 'mama'
	allowed_domains = ['mama.cn']
	start_urls = ['http://www.mama.cn/z/t666/']
	'''
	
	['http://www.mama.cn/z/t674/', 'http://www.mama.cn/z/t675/', 'http://www.mama.cn/z/t1181/',
	 'http://www.mama.cn/z/t1182/', 'http://www.mama.cn/z/t1183/', 'http://www.mama.cn/z/t666/',
	 'http://www.mama.cn/z/t1184/', 'http://www.mama.cn/z/t665/', 'http://www.mama.cn/z/t20001/',
	 'http://www.mama.cn/z/t20021/', 'http://www.mama.cn/z/t200319/', 'http://www.mama.cn/z/t200237/',
	 'http://www.mama.cn/z/t200246/', 'http://www.mama.cn/z/t200250/', 'http://www.mama.cn/z/t200256/',
	 'http://www.mama.cn/z/t3001/', 'http://www.mama.cn/z/t3002/', 'http://www.mama.cn/z/t3003/',
	 'http://www.mama.cn/z/t3004/', 'http://www.mama.cn/z/t3005/', 'http://www.mama.cn/z/t200363/',
	 'http://www.mama.cn/z/t200367/', 'http://www.mama.cn/z/t200335/', 'http://www.mama.cn/z/t200340/',
	 'http://www.mama.cn/z/t200346/', 'http://www.mama.cn/z/t200371/', 'http://www.mama.cn/z/t200376/',
	 'http://www.mama.cn/z/t200390/', 'http://www.mama.cn/z/t200393/']
	 '''
	rules = [
		Rule(LinkExtractor(restrict_xpaths=('//div[@class="list-left"]')),callback='parse_item')

	]
	def parse_item(self, response):
		data=MamaBaike()
		sel= Selector(response)
		title = response.xpath('//h1/text()').extract()[0]
		summary=response.xpath('//div[@class="detail-summary"]').extract()[0]
		label=response.xpath('//div[@class="g-ctnBar"]/a/text()').extract()[2:-1]
		cont=response.xpath('//div[@class="box mb15 mt10"]/node()')[-4:-1:2].xpath('string(.)').extract()
		d={}
		d['title'] = title
		d['summary'] = summary
		d['content'] = cont
		d['label'] = label
		yield d