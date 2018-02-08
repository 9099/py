# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
#from sun.items import Gupiaozhishi

class GupiaozhishiSpider(CrawlSpider):
	name = 'gupiaozhishi'
	allowed_domains = ['net767.com']
	start_urls = ['http://www.net767.com/gupiao/stock/']

	rules = [
		# Rule(LinkExtractor(restrict_xpaths=('//div[@class="showpage"]/a[contains(text(),"下")]'))),
		Rule(LinkExtractor(restrict_xpaths=('//p[contains(@style,"MARGIN-TOP: 2px")]')),callback='parse_item'),
		Rule(LinkExtractor(restrict_xpaths=('//p[contains(@style,"MARGIN-TOP: 5px")]')),callback='parse_item'),

	]
	def parse_item(self, response):
		cont=''

		try:
			title =''.join(response.xpath('//h1/text()').extract())
		except:
			url = ''.join(response.xpath('//script').re(r'/.+?.html'))
			url=response.urljoin(url)

			yield scrapy.Request(url,callback=self.parse_item)
			return
		# summary = response.xpath('//div[@class="art_desc mt10"]').extract()[0]

		# label=response.xpath('//div[@class="box mb15 mt10"]/node()')[-4:-1:2].xpath('string(.)').extract()
		if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
			label = response.xpath('//div[@class="g-ctnBar"]/a/text()').extract()[2:-1]
		if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
			label =response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]
		else:
			label=''
		try:
			url = response.xpath('//div[@id="pagebar"]/a[contains(text(),"下")]/@href').extract()[-1]

			if url:
				url = response.urljoin(url)
				cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract()[:-1])
				yield scrapy.Request(url, callback=self.parse_next_item,meta={'content':cont})
		except:
			cont = ''.join(response.xpath('//td[@class="neirong"]/font/*').extract())
			d = {}
			d['title'] = title
		# d['summary'] = summary
			d['content'] = cont
			d['label'] = label

			yield d
	def parse_next_item(self, response):
		cont = response.meta['content']
		try:
			url = response.xpath('//div[@id="pagebar"]/a[contains(text(),"下")]/@href').extract()[-1]
			if url:
				url = response.urljoin(url)
				cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract()[:-1])
				yield scrapy.Request(url, callback=self.parse_next_item, meta={'content': cont})
			# else:
			# 	cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract())
		except:
			cont += ''.join(response.xpath('//td[@class="neirong"]/font/*').extract()[:-1])
			d = {}
			d['title'] = response.xpath('//h1/text()').extract()[0]
			# d['title'] = title
			# d['summary'] = summary
			if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
				label = response.xpath('//div[@class="g-ctnBar"]/a/text()').extract()[2:-1]
			if response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]:
				label = response.xpath('//td[@class="bar20"]/a/text()').extract()[1:]
			else:
				label = ''
			d['content'] = cont
			d['label'] = label

			yield d
