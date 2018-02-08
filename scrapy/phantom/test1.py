# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Administrator'
js = '''
function scrollToBottom() {

    var Height = document.body.clientHeight,
        screenHeight = window.innerHeight,
        INTERVAL = 600,
        delta = 600,
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
        scroll();
    }, INTERVAL)
}
scrollToBottom()
'''
jsaaa ='''
function scrollToBottom() {

    var Height = document.body.clientHeight,  //文本高度
        screenHeight = window.innerHeight,  //屏幕高度
        INTERVAL = 300,  // 滚动动作之间的间隔时间
        delta = 500,  //每次滚动距离
        curScrollTop = 0;    //当前window.scrollTop 值

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){   //滚动到页面底部时，结束滚动
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
}
'''
js1 = '''
function a(){
var page = require('webpage').create();
page.open('http://toutiao.com', function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.render('example.png');
    }
    phantom.exit();
});}
a()
'''

driver = webdriver.PhantomJS()
driver.get("http://365yg.com/group/6414354617136234754/")
content = driver.page_source.encode('utf-8')
print(len(content))
print((content ))

# for i in range(10):
#     driver.execute_script(js)
#     time.sleep(3)
#
#
# # driver.execute_script(js1)
# content1 = driver.page_source.encode('utf-8')
# print(len(content1))
driver.quit()

jss = '''
var page = require('webpage').create();
page.open('http://www.toutiao.com', function() {

    page.render('aaaaa.jpg')
#     phantom.exit()
#   });
# });
'''

# web = webdriver.PhantomJS()
# web.implicitly_wait(25)
# web.get("http://www.toutiao.com")
# # ele = web.find_element_by_id("kw")
# web.execute_script("phantom.render('aa.jpg')")
# # ele.send_keys("java")
# hao = web.find_element_by_class_name("refresh-mode")
# hao.click()
# WebDriverWait(web,10).until()
# print(str(web.page_source))

# WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

# expected_conditions
#
# expected_conditions是selenium的一个模块，其中包含一系列可用于判断的条件：


#  ===========until param
# selenium.webdriver.support.expected_conditions（模块）
# 这两个条件类验证title，验证传入的参数title是否等于或包含于driver.title
# title_is
# title_contains
# 这两个人条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, 'kw')
# 顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
# presence_of_element_located
# presence_of_all_elements_located
# 这三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement
# 第一个和第三个其实质是一样的
# visibility_of_element_located
# invisibility_of_element_located
# visibility_of
# 这两个人条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# 这个条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
# frame_to_be_available_and_switch_to_it
# 这个条件判断是否有alert出现
# alert_is_present
# 这个条件判断元素是否可点击，传入locator
# element_to_be_clickable
# 这四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组
# 第三个传入WebElement对象以及状态，相等返回True，否则返回False
# 第四个传入locator以及状态，相等返回True，否则返回False
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# 最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
# staleness_of

