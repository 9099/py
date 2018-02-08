# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sun.items import MamaQuanzi
# from scrapy.pipelines.images import ImagesPipeline

class MamaSpider(CrawlSpider):
	name = 'mamaquanzi'
	allowed_domains = ['mama.cn']
	start_urls = ['http://q.mama.cn/topic/45394477/']
	# rules = [
	# 	Rule(LinkExtractor(allow=(r'http://www.mama.cn/z/\d+/'),restrict_xpaths=('//h5')),callback='parse_item')
	#
	# ]
	def parse_item(self, response):
		data=MamaBaike()
		sel= Selector(response)
		data['title'] = sel.xpath('//h1/text()').extract()[0].encode('utf-8').decode('utf-8')
		data['link'] = sel.xpath('//div[@class="detail-summary"]').xpath('string(.)').extract()
		yield data

	def parse_start_url(self, response):
		data=MamaQuanzi()
		title=response.xpath('//div[@class="h2box"]/a/text()').extract()[0]
		content=response.xpath('//div[@class="news_body"]')
		con_data=''
		for i in content.xpath('string(.)').extract():
			con_data+=i
		d1={}
		d1['title']=title
		d1['content']=con_data
		data['louzhu']=d1


		comment_data=[]
		comment=response.xpath('//div[@class="reply_box reply_list"]')
		for i in comment:
			name=i.xpath('.//label/a/text()').extract()[0]
			cont=i.xpath('.//div[@class="re_content"]').xpath('string(.)').extract()[0]
			d={}
			d['name']=name
			d['content']=cont
			comment_data.append(d)
		data['comment']=comment_data
		yield data
