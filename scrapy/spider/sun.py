# -*- coding: utf-8 -*-
import scrapy


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['99.com.cn']
    start_urls = ['http://99.com.cn/']

    def parse(self, response):
        pass
