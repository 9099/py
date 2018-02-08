# encoding:utf-8
from random import choice

__author__ = 'Administrator'
import requests
import time
import os
# sss =  "http://www.toutiao.com/api/pc/feed/?max_behot_time=%s&category=__all__&widen=1&tadrequire=false&as=A175F9D771632DD&cp=5971E302BD5D9E1"
# with open("as.v","w+") as f:
#     for i in range(10):
#         num = "1234567890"
#         s ="http://www.toutiao.com/api/pc/feed/?max_behot_time=15%s%s%s%s%s%s%s%s&category=__all__&widen=1&tadrequire=false&as=A175F9D771632DD&cp=5971E302BD5D9E1" %(choice(num),choice(num),choice(num),choice(num),choice(num),choice(num),choice(num),choice(num))+'\n'
#     # time.sleep(2)
#     # ss=choice(num)
#
#         f.write(s)
#     f.close()
#


#  os 文件操作
# 1.得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
# 2.返回指定目录下的所有文件和目录名:os.listdir()
# 3.函数用来删除一个文件:os.remove()
# 4.删除多个目录：os.removedirs(r"c：\python")
# 5.检验给出的路径是否是一个文件：os.path.isfile()
# 6.检验给出的路径是否是一个目录：os.path.isdir()
# 7.判断是否是绝对路径：os.path.isabs()
# 8.检验给出的路径是否真地存:os.path.exists()
# 9.返回一个路径的目录名和文件名:os.path.split()
# 例子：
#
#
# 复制代码 代码如下:
#
# os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
#
# 10.分离扩展名：os.path.splitext()
# 11.获取路径名：os.path.dirname()
# 12.获取文件名：os.path.basename()
# 13.运行shell命令: os.system()
# 14.读取和设置环境变量:os.getenv() 与os.putenv()
# 15.给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
# 16.指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
# 17.重命名：os.rename(old， new)
# 18.创建多级目录：os.makedirs(r"c：\python\test")
# 19.创建单个目录：os.mkdir("test")
# 20.获取文件属性：os.stat(file)
# 21.修改文件权限与时间戳：os.chmod(file)
# 22.终止当前进程：os.exit()
# 23.获取文件大小：os.path.getsize(filename)

# os.mkdir("file")
# 2.复制文件：
# shutil.copyfile("oldfile","newfile")        #oldfile和newfile都只能是文件
# shutil.copy("oldfile","newfile")            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# 3.复制文件夹：
# 4.shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在
# 5.重命名文件（目录）
# os.rename("oldname","newname")              #文件或目录都是使用这条命令
# 6.移动文件（目录）
# shutil.move("oldpos","newpos")
# 7.删除文件
# os.remove("file")
# 8.删除目录
# os.rmdir("dir")                             #只能删除空目录
# shutil.rmtree("dir")                        #空目录、有内容的目录都可以删
# 9.转换目录
# os.chdir("path")                            #换路径
if os.path.isdir("aa/aaa/aa"):
    print("目录存在")
else:
    os.mkdir("aa/aaa/aa")
# 四、文件综合操作实例
# 将文件夹下所有图片名称加上'_fc'
# python代码:
#
# 复制代码 代码如下:
#
# # -*- coding:utf-8 -*-
# import re
# import os
# import time
# #str.split(string)分割字符串
# #'连接符'.join(list) 将列表组成字符串
# def change_name(path):
#     global i
#     if not os.path.isdir(path) and not os.path.isfile(path):
#         return False
#     if os.path.isfile(path):
#         file_path = os.path.split(path) #分割出目录与文件
#         lists = file_path[1].split('.') #分割出文件与文件扩展名
#         file_ext = lists[-1] #取出后缀名(列表切片操作)
#         img_ext = ['bmp','jpeg','gif','psd','png','jpg']
#         if file_ext in img_ext:
#             os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
#             i+=1 #注意这里的i是一个陷阱
#         #或者
#         #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
#         #if file_ext in img_ext:
#         #    print('ok---'+file_ext)
#     elif os.path.isdir(path):
#         for x in os.listdir(path):
#             change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用
#
# img_dir = 'D:\\xx\\xx\\images'
# img_dir = img_dir.replace('\\','/')
# start = time.time()
# i = 0
# change_name(img_dir)
# c = time.time() - start
# print('程序运行耗时:%0.2f'%(c))
# print('总共处理了 %s 张图片'%(i))

path ='C:Users\Administrator\Desktop\scrapy\\test\\aa\\a'


