# -*- coding: utf-8 -*-
import scrapy
import chardet
from scrapy.http import FormRequest, Request
from sun.items import AlimamaItem

class AlimamaSpider(scrapy.Spider):
    name = 'alimama'
    allowed_domains = ['alimama.com']
    start_urls = ['pub.alimama.com']
    header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
        "Origin":"http://diguo1.com",

    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Referer": "http://diguo1.com/e/member/login/",
        "Cookie":"__guid=45918257.1529121458185236500.1501907735500.393; monitor_count=17"
    }
    cook ={'Host': 'diguo1.com', 'Connection': 'keep-alive', 'Content-Length': '102', 'Cache-Control': 'max-age=0', 'Origin': 'http', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Referer': 'http', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8'}
    header1 =  {'Host': 'diguo1.com', 'Connection': 'keep-alive', 'Content-Length': '102', 'Cache-Control': 'max-age=0', 'Origin': 'http', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Referer': 'http', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8'}
    def start_requests(self):
        return [FormRequest("http://diguo1.com/e/member/doaction.php",headers=self.header1,formdata={'ecmsfrom': '', 'enews': 'login', 'tobind': '0', 'username': 'cococo', 'password': 'mnbvcx', 'lifetime': '0', 'Submit': '+%E7%99%BB+%E5%BD%95+'})]
    # def start_requests(self):
    #     return [Request("http://diguo1.com/e/member/doaction.php", callback = self.post_login)]  #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    #
    # #FormRequeset
    # def post_login(self, response):
    #
    #     #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
    #     #登陆成功后, 会调用after_login回调函数
    #     return [FormRequest(response,
    #                         # formdata = {
    #                         #
    #                         # 'email': '123456',
    #                         # 'password': '123456'
    #                         # },
    #
    #                         formdata={'ecmsfrom': '', 'enews': 'login', 'tobind': '0', 'username': 'cococo', 'password': 'mnbvcx', 'lifetime': '0', 'Submit': '+%E7%99%BB+%E5%BD%95+'},
    #                         headers=self.header1,
    #                         callback = self.after_login
    #                         )]
    # def after_login(self, response) :
    #     print(response.body.decode())
    def parse(self, response):
        print(response.body.decode())
