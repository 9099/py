# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver


js ='''
function scrollToBottom() {

    var Height = document.body.clientHeight,
        screenHeight = window.innerHeight,
        INTERVAL = 400,
        delta = 800,
        curScrollTop = 0;

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;

        scroll();
    }, INTERVAL)
}
scrollToBottom();
'''
# if (curHeight >= Height){
#             clearInterval(timer);
#         }

class PhantomJSMiddleware(object):
    @classmethod


    def process_request(cls, request, spider):

        if request:

            driver = webdriver.PhantomJS()
            # driver.set_window_size(500,500)
            driver.get(request.url)
            # ele = driver.find_element_by_class_name("refresh-mode")
            # ele.click()
            s = driver.page_source.encode('utf-8')
            # print(len(s),"=====================1=====================a")
            # for i in range(3):
            #
            #     driver.execute_script(js)
            #     time.sleep(3)
                # (driver.page_source.encode('utf-8'))
            # driver.execute_script(js)
            # time.sleep(5)

            content = driver.page_source.encode('utf-8').decode()
            # print(content)
            # print(len(content),"========================2===================b")
            driver.quit()
            # print("middle=========================================")

            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)

class PhantomJSMiddleware1(object):
    @classmethod


    def process_request(cls, request, spider):

        if request:

            driver = webdriver.PhantomJS()
            # driver.set_window_size(500,500)
            driver.get(request.url)
            # ele = driver.find_element_by_class_name("refresh-mode")
            # ele.click()


            content = driver.page_source.encode('utf-8').decode()
            # print((content),"=====================================")

            driver.quit()


            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
    def process_response(request, response, spider):
        return response
class SunSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
