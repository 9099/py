# coding: utf-8
import scrapy
from sun.items import SunItem
from sun.items import NextItem

class JiankangSpider(scrapy.Spider):
    name = 'jiankang'
    allowed_domains = ['99.com.cn']
    start_urls = ['http://www.99.com.cn/erbihou/ebjb/']

    def parse(self, response):

        for it in response.xpath('//*[@id="page"]/div[2]/div[1]/div[2]/div[1]/div'):
            item = SunItem()
            title = item['title'] = ''.join(it.xpath('h2/a/text()').extract()).encode('utf-8')

            yield (item)
            
        nextitem =NextItem()
        url = nextitem['next_url'] = "http://www.99.com.cn/erbihou/ebjb/"+''.join(it.xpath('//*[@id="page"]/div[2]/div[1]/div[2]/div[2]/span[2]/a/@href').extract())
        #data.append(nextitem)
        yield nextitem
        request = scrapy.Request(url,self.parse,meta={'i':True})

        yield request

