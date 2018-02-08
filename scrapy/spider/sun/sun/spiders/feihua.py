# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FeihuaSpider(CrawlSpider):
	name = 'feihua'
	allowed_domains = ['fh21.com.cn']
	start_urls = ['http://jianfei.fh21.com.cn/ys/sp/']



	rules = [
		# Rule(LinkExtractor(restrict_xpaths=('//div[@class="wrap-list-paging mt-20"]//a[contains(text(),"下")]')),follow=True),
		Rule(LinkExtractor( restrict_xpaths=('//div[@class="ls-mod"]//a'),unique=True), callback='parse_item'),
	]

	def next_url(self, response):
		try:
			url = ''.join(response.xpath('//div[@class="wrap-list-paging mt-20"]//a[contains(text(),"下")]/@href').extract())

			if url:
				url = response.urljoin(url)
				return url
			else:
				url = ''
				return url
		except:
			return

	def parse_item(self, response):

		url = self.next_url(response)
		if url:
			cont = ''.join(response.xpath('//div[@class="art_con"]').extract())
			yield scrapy.Request(url, callback=self.parse_next_item, meta={'data': cont})
		else:
			d = self.extract_data(response)
			yield d

	def extract_data(self, response):
		d = {}
		title = ''.join(response.xpath('//div[@class="arti-head"]/h2/text()').extract())
		# summary = ''.join(response.xpath('//p[@class="summary"]').extract())
		cont = ''.join(response.xpath('//div[@class="arti-content"]').extract())
		label = response.xpath('//div[@class="bread clearfix"]//a/text()').extract()[1:]
		# from_ = ''.join(response.xpath('//div[@class="date"]//a/text()').extract())
		d['title'] = title
		# d['summary'] = summary
		# d['from'] = from_
		d['content'] = cont
		d['label'] = label
		return d

	def parse_next_item(self, response):
		cont = response.meta['data']
		cont += ''.join(response.xpath('//div[@class="art_con"]').extract())
		url = self.next_url(response)
		if url:
			yield scrapy.Request(url, callback=self.parse_next_item, meta={'data': cont})
		else:
			d=self.extract_data(response)
			yield d