# -*- coding: utf-8 -*-
import scrapy
from sun.items import SunItem

class HuabanSpider(scrapy.Spider):
    name = 'huaban'
    allowed_domains = ['huaban.com']
    start_urls = ['http://huaban.com/explore/fensehunli/']

    def parse(self, response):
        for it in response.xpath('//a[@class="img x layer-view loaded"]'):
            item = SunItem()
            item['title']=it.xpath('.//img/@src').extract()[0]
            yield item