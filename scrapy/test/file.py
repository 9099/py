# coding:utf-8
import os
import random
import stat
import time

__author__ = 'Administrator'
# 修改目录下的照片文件
# def change(path):
#     if not os.path.isdir(path):
#         print("Error")
#     else:
#         list = os.listdir(path)
#         for it in list:
#             name = it.split('.')
#             type = name[1]
#             if type in ['jpg','png']:
#                 os.rename(it,'sun'+it)
# print(os.listdir(r'C:\Users\Administrator\Desktop\scrapy\test'))
# change(r'C:\Users\Administrator\Desktop\scrapy\test')
# print(os.listdir(r'C:\Users\Administrator\Desktop\scrapy\test'))
# list = os.listdir(r'C:\Users\Administrator\Desktop\scrapy\test')
# name = list[1].split('.')
# print(name)
# sep = os.path.sep
# os.makedirs(r'C:\Users\Administrator\Desktop\scrapy\test\file\a\e\f\e')
# os.chmod(r'C:\Users\Administrator\Desktop\scrapy\test\file\a\e\f\e',777)
# os.remove(r'C:\Users\Administrator\Desktop\scrapy\test\file\a\e\f\e')
# os.mknod('False.txt',stat.S_IFCHR)
# os.mk

# requests 库的使用
# import requests
# s =requests.post('')
# 字符串拼接
# ss = r'afegegs#skofdo#s'
# aa = ss.split('#',1)
# print(aa)

# re模块
# import re
# str = r'1232jidsmkgmrk^sijdi*'
# print(re.match(r'(.*?)m(.*?).*',str).group(1))
# print(re.match(r'(.*?)m(.*?).*',str).group(0))
# print(re.match(r'(.*?)m(.*?).*',str).group())


# import json
# s = r'{"nema":12,"age":23}'
# sss =json.loads(s)
# print(sss)


# import jieba.analyse
# jie1 = jieba.analyse.ext ract_tags("我要去上学了，你去不去，我们一起去吧！我要去上学了，你去不去，我们一起去吧！我要去上学了，你去不去，我们一起去吧！",topK=3)
# jie = jieba.analyse.default_textrank(jie1,topK=4)
# print(jie)
# print(' '.join(jie1))

# ada = 'abcdefghijklmnopqrstuvwxyz1234567890'
# print(random.choice(ada) )
# start = time.time()
# with open("rand.txt",'r') as f:
#     for i in range(10000):
#         jie = 'www.baidu.com/?index%s%s%s%s%s'%(random.choice(ada),random.choice(ada),random.choice(ada),random.choice(ada),random.choice(ada))
#         # f.write(jie+'\n')
#     print(len(f.readlines()))
# end = time.time()
# print(end-start)
#
# with open('rand.txt','r') as f:
#
#
#     print()

dd = {"sde":{"fsd":2}}
print(dd['sde']['fsd'])