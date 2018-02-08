__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from selenium import webdriver

drivers =webdriver.PhantomJS()
drivers.get("http://toutiao.com")
print(drivers.page_source.encode('utf-8'))


#


