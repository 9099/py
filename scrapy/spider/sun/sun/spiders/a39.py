# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class A39Spider(CrawlSpider):
	name = '39'
	allowed_domains = ['39.net']
	start_urls = ['http://xl.39.net/xltm/xlcs/']

	rules = [
		# Rule(LinkExtractor(restrict_xpaths=('//div[@class="list_page"]//a[contains(text(),"下")]')),follow=True),
		Rule(LinkExtractor(allow=('.+?151028.+?'),restrict_xpaths=('//div[@class="listbox"]')),callback='parse_item'),
	]
	def next_url(self,response):
		try:
			url=''.join(response.xpath('//div[@class="art_page"]//a[contains(text(),"下")]/@href').extract())

			if url:
				url = response.urljoin(url)
				return url
			else:
				url=''
				return url
		except:
			return
	def parse_item(self, response):



		url=self.next_url(response)
		if url:
			cont = ''.join(response.xpath('//div[@class="art_con"]').extract())
			yield scrapy.Request(url,callback=self.parse_next_item,meta={'data':cont})
		else:
			d = {}
			label = response.xpath('//span[@class="art_location"]//a/text()').extract()[1:]
			title = response.xpath('//h1/text()').extract()[0]
			from_ = ''.join(response.xpath('//div[@class="date"]//a/text()').extract())
			summary = ''.join(response.xpath('//p[@class="summary"]').extract())
			cont = ''.join(response.xpath('//div[@class="art_con"]').extract())
			d['title'] = title
			d['summary'] = summary
			d['from'] = from_
			d['content'] = cont
			d['label'] = label
			yield d

	def parse_next_item(self, response):
		cont=response.meta['data']
		cont+=''.join(response.xpath('//div[@class="art_con"]').extract())
		url=self.next_url(response)
		if url:
			yield scrapy.Request(url,callback=self.parse_next_item,meta={'data':cont})
		else:
			d = {}
			label = response.xpath('//span[@class="art_location"]//a/text()').extract()[1:]
			title = response.xpath('//h1/text()').extract()[0]
			from_ = response.xpath('//div[@class="date"]//a/text()').extract()[0]
			summary = ''.join(response.xpath('//p[@class="summary"]').extract())
			cont = ''.join(response.xpath('//div[@class="art_con"]').extract())
			d['title'] = title
			d['summary'] = summary
			d['from'] = from_
			d['content'] = cont
			d['label'] = label
			yield d