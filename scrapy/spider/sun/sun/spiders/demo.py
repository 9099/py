# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils import url
from scrapy.utils.response import get_base_url

from sun.items import Demo
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from twisted.web.http import urlparse
from w3lib.url import urljoin_rfc


class DemoSpider(scrapy.Spider):
	name = 'demo'
	allowed_domains = ['hupu.com']
	start_urls = [

		'https://voice.hupu.com/soccer/2195800.html',
		'https://voice.hupu.com/soccer/2198981.html',
	              ]


	# def parse(self, response):
	# 	cont=''
	#
	# 	title =response.xpath('//h1/text()').extract()[0]
	# 	# summary = response.xpath('//div[@class="art_desc mt10"]').extract()[0]
	#
	# 	# label=response.xpath('//div[@class="box mb15 mt10"]/node()')[-4:-1:2].xpath('string(.)').extract()
	# 	if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
	# 		label = response.xpath('//div[@class="g-ctnBar"]/a/text()').extract()[2:-1]
	# 	if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
	# 		label =response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]
	# 	else:
	# 		label=''
	# 	url = response.xpath('//div[@id="pagebar"]/a[contains(text(),"下")]/@href').extract()[-1]
	#
	# 	if url:
	# 		url = response.urljoin(url)
	# 		cont = ''.join(response.xpath('//td[@class="neirong"]/font/*').extract()[:-1])
	# 		yield scrapy.Request(url, callback=self.parse_next_item,meta={'content':cont})
	# 	# else:
	# 	# 	cont = ''.join(response.xpath('//td[@class="neirong"]/font/*').extract())
	# 	# d = {}
	# 	# # d['title'] = title
	# 	# # # d['summary'] = summary
	# 	# d['content'] = cont
	# 	# d['label'] = label
	# 	#
	# 	# yield d
	def parse_next_item(self, response):
		cont=response.meta['content']
		try:
			url = response.xpath('//div[@id="pagebar"]/a[contains(text(),"下")]/@href').extract()[-1]


			url = response.urljoin(url)
			cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract()[:-1])
			yield scrapy.Request(url, callback=self.parse_next_item, meta={'content': cont})
		except:
			cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract())
			d = {}
			d['title']=response.xpath('//h1/text()').extract()[0]
			# d['title'] = title
			# d['summary'] = summary
			d['content'] = cont
			# d['label'] = label

			yield d
	def parse(self, response):
		data=Demo()
		# base=get_base_url(response)
		# content=response.xpath('//div[@class="list-box article-box"]')
		# urls=
		data['image_urls']=response.xpath('//div[@class="artical-content"]//img/@src').extract()
		data['content']=''.join(response.xpath('//div[@class="artical-content"]').extract())
		data['title']='aaaa'
		yield data
		# get_base_url
		# url.urljoin_rfc()
