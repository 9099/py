# -*- coding: utf-8 -*-
import scrapy
from sun.items import TouTiaoTechItem

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://www.toutiao.com/ch/news_tech/']

    def parse(self, response):
        #for it in response.xpath('//div[@class="y-left"]'):
        for it in response.xpath('//li[@ga_event="article_item_click"]'):
            tech = TouTiaoTechItem()
            tech['title'] = it.xpath('.//a[@class="link title"]/text()').extract()[0].strip()
            tech['url'] ='http://www.toutiao.com'+ it.xpath('.//a[@class="link title"]/@href').extract()[0].strip()
            tech['author'] = (it.xpath('.//a[@class="lbtn source"]/text()').extract()[0][:-1]).strip()
            tech['author_url'] = 'http://www.toutiao.com'+ it.xpath('.//a[@class="lbtn source"]/@href').extract()[0].strip()
            tech['author_avatar'] =  it.xpath('.//a[@class="lbtn media-avatar"]/img/@src').extract()[0].strip()
            tech['comment_num'] =it.xpath('.//a[@class="lbtn comment"]/text()').extract()[0][:-1].strip()
            title_img = it.xpath('.//a[@class="img-wrap"]/img/@src').extract()
            if title_img:
                tech['title_img'] =title_img[0].strip()
            tech['group_id'] =it.xpath('.//span[@class="dislike"]/@data-groupid').extract()[0].strip()
            yield tech

