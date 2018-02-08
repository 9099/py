#encoding:utf-8
from collections import Iterator

import requests
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s1 = [x for x in range(1000)]
s2 = (x for x in range(1000))
# print(sys.getsizeof(s1))
# print(s1)
# print(sys.getsizeof(s2))
# print(s2)

import selenium
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
if (curHeight >= Height){
            clearInterval(timer);
        }
    }, INTERVAL)
}
scrollToBottom();
'''
from selenium import webdriver
url = 'http://www.toutiao.com/ch/video/'

driver = webdriver.PhantomJS()  # driver.set_window_size(500,500)
driver.set_window_size(480,300)
driver.get(url)
time.sleep(0.5)
# ele = driver.find_element_by_class_name("refresh-mode")
# ele.click()
s = driver.page_source.encode('utf-8').decode()
print(len(s), "=====================1=====================a")
# print((s), "=====================1=====================a")
# for i in range(3):
#
#     driver.execute_script(js)
#     time.sleep(3)
# (driver.page_source.encode('utf-8'))
# driver.execute_script(js)
time.sleep(5)
driver.save_screenshot("1.jpg")
# for iii in range(37):
#     # driver.refresh()
#     try:
#         ele = driver.find_element_by_class_name('list-refresh-msg')
#         # src = ele.get_attribute("innerHTML")
#         ele.click()
#         # driver.refresh()
#         time.sleep(0.4)
#     except :
#         print("a")
#         continue
#     # try:
#     #     # ele = driver.find_element_by_class_name('list-refresh-msg')
#     #     element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, 'list-refresh-msg')))
#     #
#     # except:
#     #     print("Time out")
#     #     continue
#
#
#     time.sleep(4)

# driver.execute_script(js)
click = '''
function click1() {
    var a = document.getElementsByTagName("a");
    a[101].click();
}
click1();
'''
# driver.execute_script(click)
#
#
# time.sleep(0.5)
# # driver.refresh()
# time.sleep(5)
# driver.save_screenshot("2.jpg")
# content = driver.page_source.encode('utf-8').decode()
# # print(content)
# print(len(content), "========================2===================b")
# # print((content), "========================2===================b")
# driver.quit()
