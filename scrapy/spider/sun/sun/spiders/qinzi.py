# -*- coding: utf-8 -*-
import scrapy
# from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QinziSpider(CrawlSpider):
    name = 'qinzi'
    allowed_domains = ['qinzi.com.cn']
	#   45  53  46 3 
    start_urls = ['http://www.qinzi.com.cn/index.php?m=cms&q=list&column=45','http://www.qinzi.com.cn/index.php?m=cms&q=list&column=46',
		'http://www.qinzi.com.cn/index.php?m=cms&q=list&column=53','http://www.qinzi.com.cn/index.php?m=cms&q=list&column=3'
	]

    rules = [
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="topic_list_top_left"]/div/a[@class="pages_next"]')),follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="topic_list_top_left"]/ul')),callback='parse_item')
    ]

    def parse_item(self, response):
        d = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        label=response.xpath('//div[@id="list_nav"]/a/text()').extract()
        title=response.xpath('//b[@class="article_title"]/text()').extract()[0]
        summary=''.join(response.xpath('//div[@id="content_wenzi"]/span').xpath('string(.)').extract()).strip()
        cont=response.xpath('//div[@id="baby_pic_wenzi"]').extract()[0]
        d['title'] = title
        d['summary'] = summary
        d['content'] = cont
        d['label'] = label
        yield d
