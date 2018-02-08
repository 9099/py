#encoding:utf-8
# import scrapy
# url =>  request =scrapy.Request()
# request.meta['phantomjs'] = True
# yield request
#
# # middleware
# class Middle(object):
#     @classmethod
#     def process(cls,request,spider):
#         if(request.meta.has_key('phantomjs')):
#             driver = wendriverr.Phantomjs()
#             driver.get(request.url)
#             content = driver.page_resource.encode(utf8)
#             driver.quit()
#             return HtmlResponde(request.rul,encodingutf8,body=content,request=request)

# global sum
# sum = 0
# def do(i):
#     for ia in range(i,i+60):
#         ia+=1
#         print(ia)
#         global sum
#         sum =ia
#
# import sys
# s=sys.argv[1]
# s=int(s)
# do(s)
#
# with open("i","w+") as f:
#     f.write(str(sum))
import json
import random
import time
import timeit

s='''
Host: diguo1.com
Connection: keep-alive
Content-Length: 102
Cache-Control: max-age=0
Origin: http://diguo1.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://diguo1.com/e/member/login/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8


'''
# s1 ='ecmsfrom=&enews=login&tobind=0&username=cococo&password=mnbvcx&lifetime=0&Submit=+%E7%99%BB+%E5%BD%95+'
# s = s.strip().split('\n')
# s = {x.split(':',maxsplit=1)[0] : x.split(':',maxsplit=1)[1].strip() for x in s}
# print(s)
# s1 = s1.split('&')
#
# s1={x.split('=')[0]:x.split('=')[1] for x in s1}
# print(s1)

cook = '''
__guid=45918257.1000756604606952100.1501920606675.7456
	rkoryecmsdodbdata=empirecms
	rkoryloginuserid=1
	rkoryloginusername=admin
	rkoryloginrnd=zLHF5e1jxRVOxZLUD3Wp
	rkoryloginlevel=1
	rkoryeloginlic=empirecmslic
	rkoryloginadminstyleid=1
	rkoryloginecmsckpass=d4a5f373b5287ccbb5b4450f2c4c064a
	rkoryloginecmsckfrnd=M5BitzAQREhv92MpfUuRJLXMK7Y
	rkorytruelogintime=1501920773
	rkorylogintime=1501920780
	gcuxnreturnurl=http%3A%2F%2Fdiguo1.com%2F
	monitor_count=46
'''
# cook=cook.strip().split('\n')
# cook={i.strip().split('=')[0] :i.strip().split('=')[1] for i in cook}
# print(cook)
#
# cook1  = "__guid=45918257.1000756604606952100.1501920606675.7456; rkoryecmsdodbdata=empirecms; rkoryloginuserid=1; rkoryloginusername=admin; rkoryloginrnd=zLHF5e1jxRVOxZLUD3Wp; rkoryloginlevel=1; rkoryeloginlic=empirecmslic; rkoryloginadminstyleid=1; rkoryloginecmsckpass=d4a5f373b5287ccbb5b4450f2c4c064a; rkoryloginecmsckfrnd=M5BitzAQREhv92MpfUuRJLXMK7Y; rkorytruelogintime=1501920773; rkorylogintime=1501920780; monitor_count=65"
# cook1=cook1.strip().split(';')
# cook1={i.strip().split('=')[0] :i.strip().split('=')[1] for i in cook1}
# print(cook1)
# def a():
# 	print("a")
# def b(cc):
# 	def c():
# 		cc()
# 		time.sleep(1)
# 		end=time.clock()
# 		# if end-start>10:
# 		# 	exit(0)
# 		r="5"
# 		# return r
# 	# print(r)
# 	return c
#
# start = time.clock()
# # bb=b("ccc")
# # bb()
# @b
# def pri():
# 	print("print")
#
# end=time.clock()
#
# print(end - start)
# print(timeit.timeit(stmt=pri))
# &max_behot_time=1502106814&max_behot_time_tmp=1502106814&tadrequire=true&as=A145F928B8746C6&cp=598854061C060E1
s='''{
			"content":"{"log_pb": {"impr_id": "20170808152544010008043076890507"}, "read_count": 161481, "media_name": "\u897f\u695a\u7f51", "ban_comment": 0, "abstract": "\u4e0a\u6d77\u95f5\u884c\u201c\u56e0\u6392\u961f\u625375\u5c81\u8001\u4eba\u8033\u5149\u201d\u7684\u7537\u5b50\u8eab\u4efd\u5df2\u786e\u5b9a\uff1a\u7cfb\u4e0a\u6d77\u4e0014\u5c81\u521d\u4e2d\u751f\u30028\u67087\u65e5\uff0c\u6f8e\u6e43\u65b0\u95fb\u8bb0\u8005\u4ece\u8b66\u65b9\u83b7\u6089\uff0c\u7ecf\u95f5\u884c\u4e03\u5b9d\u6d3e\u51fa\u6240\u8fde\u65e5\u6392\u67e5\uff0c\u6253\u4eba\u7537\u5b50\u6768\u67d0\u5df2\u4e8e\u5f53\u65e5\u4e0a\u5348\u88ab\u5e26\u8fdb\u6d3e\u51fa\u6240\u8c03\u67e5\u3002", "image_list": [], "ugc_recommend": {"reason": "", "activity": ""}, "article_type": 0, "tag": "news_society", "forward_info": {"forward_count": 1}, "has_m3u8_video": 0, "keywords": "\u6d3e\u51fa\u6240\u6c11\u8b66,\u6d3e\u51fa\u6240,\u4e0a\u6d77", "rid": "20170808152544010008043076890507", "show_portrait_article": false, "user_verified": 0, "aggr_type": 1, "cell_type": 0, "article_sub_type": 0, "bury_count": 12, "title": "\u521d\u4e2d\u751f\u56e0\u6392\u961f\u7ea0\u7eb7\u8fde\u6247\u8001\u592a\u592a\u8033\u5149 \u4fdd\u5b89\u672a\u53ca\u65f6\u5236\u6b62", "ignore_web_transform": 1, "source_icon_style": 1, "tip": 0, "hot": 0, "share_url": "http://toutiao.com/a6451446260406960398/?iid=123456789&app=news_article", "has_mp4_video": 0, "source": "\u897f\u695a\u7f51", "comment_count": 972, "article_url": "http://toutiao.com/group/6451446260406960398/", "filter_words": [{"id": "8:0", "name": "\u770b\u8fc7\u4e86", "is_selected": false}, {"id": "9:1", "name": "\u5185\u5bb9\u592a\u6c34", "is_selected": false}, {"id": "5:9312190", "name": "\u62c9\u9ed1\u4f5c\u8005:\u897f\u695a\u7f51", "is_selected": false}, {"id": "2:215598512", "name": "\u4e0d\u60f3\u770b:\u793e\u4f1a\u8d1f\u9762", "is_selected": false}], "share_count": 100, "publish_time": 1502100003, "action_list": [{"action": 1, "extra": {}, "desc": ""}, {"action": 3, "extra": {}, "desc": ""}, {"action": 7, "extra": {}, "desc": ""}, {"action": 9, "extra": {}, "desc": ""}], "cell_layout_style": 1, "tag_id": 6451446260406960398, "action_extra": "{\"channel_id\": 3189398996}", "video_style": 0, "verified_content": "", "display_url": "http://toutiao.com/group/6451446260406960398/", "large_image_list": [], "media_info": {"user_id": 4176167047, "verified_content": "", "avatar_url": "http://p2.pstatp.com/large/2760/4058194514", "media_id": 4176251026, "name": "\u897f\u695a\u7f51", "recommend_type": 0, "follow": false, "recommend_reason": "", "is_star_user": false, "user_verified": false}, "item_id": 6451470387879346702, "is_subject": false, "show_portrait": false, "repin_count": 690, "cell_flag": 11, "user_info": {"verified_content": "", "avatar_url": "http://p3.pstatp.com/thumb/2760/4058194514", "user_id": 4176167047, "name": "\u897f\u695a\u7f51", "follower_count": 0, "follow": false, "user_auth_info": "", "user_verified": false, "description": "\u897f\u695a\u7f51\u662f\u7531\u5bbf\u8fc1\u5e02\u59d4\u5ba3\u4f20\u90e8\u4e3b\u7ba1\u3001\u5bbf\u8fc1\u5e02\u5e7f\u64ad\u7535\u89c6\u603b\u53f0\uff08\u96c6\u56e2\uff09\u4e3b\u529e\u7684\u5bbf\u8fc1\u5730\u533a\u6700\u5927\u7684\u7efc\u5408\u95e8\u6237\u7f51\u7ad9\u3002"}, "source_open_url": "sslocal://profile?uid=4176167047", "level": 0, "like_count": 5, "digg_count": 5, "behot_time": 1502177113, "cursor": 1502177113999, "url": "http://toutiao.com/group/6451446260406960398/", "preload_web": 0, "user_repin": 0, "has_image": false, "item_version": 0, "has_video": false, "group_id": 6451446260406960398, "middle_image": {}}",
			"code":""
		}
		'''
# s='{"s":1,"ss":21}'
# s = json.loads(s)
# s=dict(s)
# s["as"]=123
# print(s)
#
# http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time=1502181217&last_refresh_sub_entrance_interval=1502181219&loc_mode=6&loc_time=1502180314&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123
# import random
# def parse_url():
# 	t = time.time()
# 	t = int(t)
# 	tt = t - random.randint(80, 300)
# 	# url ='http://www.toutiao.com/api/article/feed/?category=essay_joke&widen=1&max_behot_time=%s&max_behot_time_tmp=%s&tadrequire=true&as=A145F928B8746C6&cp=598854061C060E1'%(tt-random.randint(40,300),tt)
#
#
# 	url = 'http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time={0}&last_refresh_sub_entrance_interval={1}&loc_mode=6&loc_time={2}&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123'.format(tt-random.randint(20,100), tt, tt-random.randint(400,900))
# 	return url
#
# sStr1 = 'abcdefg'
# sStr2 = 'cde'
# print (sStr1.find(sStr2))
# print(parse_url())

import sys
import os
import multiprocessing
def p(name):
	print("Task %s (%s)"%(name,os.getpid()))
	time.sleep(random.random()*20)
def p2(name):
	print("Task2222 %s (%s)"%(name,os.getpid()))
	time.sleep(random.random()*20)

# if __name__=='__main__':
# 	print('Parent %s'%os.getpid())
# 	pool = multiprocessing.Pool(7)
# 	for i in range(12):
# 		mes="T%s"%(i)
# 		pool.apply_async(p,args=(mes,))
# 	print("Waiting all done")
#
# 	pool.close()
# 	pool.join()
# 	print("All done")

j='''
{
	"has_more":true,
	"message":"success",
	"data":123,
	"next":{
		"max_behot_time":1502271245
	}
}
'''
import pymongo
def init_database(collection):
	global coll
	conn = pymongo.MongoClient(host='115.159.98.124', port=27017)
	db = conn.get_database('toutiao')
	coll=db.get_collection(collection)
	# sel = 'ceshi%s'%(collection)
	# coll = db.create_collection(collection)

	coll.insert_one({'x':2})
	return coll
# init_database("fegs")
import numpy as np
# n=np.arange(15).reshape(3,5)
# # n=np.zeros((3,3))
# print(dir(n))

def parse_url(category):
	t = time.time()
	t = int(t)
	tt = t - random.randint(80, 300)
	url ='http://www.toutiao.com/api/article/feed/?category={0}&widen=1&max_behot_time={1}&max_behot_time_tmp={2}&tadrequire=true&as=A145F928B8746C6&cp=598854061C060E1'.format(category,tt-random.randint(40,300),tt)
	# url = 'http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time={0}&last_refresh_sub_entrance_interval={1}&loc_mode=6&loc_time={2}&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123'.format(tt-random.randint(20,100), tt, tt-random.randint(400,900))
	return url
# print(parse_url("video"))


s='.avi | .dat | .mpg | .mpeg | .vob | .mkv | .mov | .wmv | .asf | .rm | .rmvb | .ram | .flv | .mp4 | .3gp | .dv | .qt | .divx | .cpk | .fli | .flc | .m4v'
# s=s.split('|')
# ss=[]
# for i in s:
# 	i=i.split('.')
# 	ss.append(i[1])
# url='http://vali.cp31.ott.cibntv.net/6572E7B882E38715E409527F9/0300020700598BB60C4375011BA6A9F4609550-4FE2-A36E-B9CC-670744F56BBC.'
#
# url ='http://cloud.video.taobao.com/play/u/2821843773/p/1/e/1/t/1/fv/102/38962733.swf'
# # to  http://cloud.video.taobao.com/play/u/2821843773/p/1/e/6/t/1/39199228.mp4
#
#
#
# # taobao2mp4(url)
# s={"offset":0,"filter":"all","tab":"rec","direction":"down","auto":0,"h_av":"3.6.4","h_dt":0,"h_os":22,"h_model":"m3 note","h_did":"862143030414424_a4:44:d1","h_nt":1,"h_m":34187505,"h_ch":"meizu","h_ts":1502456474058,"token":"T0KeNAplOdT3n8QV5PPjA3KEABOEdUpTn5ahS81yccP00Kuk="}
# ss=''
# # for k,v in s.items():
# s='https://whois.aliyun.com/whois/api_whois_full?host=sdfd.com&web_server=whois.uniregistrar.com&umToken=whois-web-hichina-com%3Acf13f1eafd0143c61e16265c646d6928&_={0}'.format(int(time.time()*1000))
#
#
# print(s)

import jieba
import jieba.analyse
import jieba.posseg
# j=jieba.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# jj=jieba.posseg.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# jjj=jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# # print(','.join(j))
# for i,j in jj:
# 	print(i,j)
# # print(','.join(jjj))
# print(jieba.analyse.extract_tags('小明硕士毕业于中国科学院计算所，后在日本京都大学深造',topK=5,allowPOS=('v','n','d')))
import csv
# with open('as.csv','w') as f:
# 	for i in range(40):
# 		s='%s,%s,%s,%s\n'%(i,i+1,i+2,str(i+3)+"你好")
#
# 		print(f.tell())
# 		f.writelines(s)
import time
ti='2017,8,14-14,52,43'
print(time.mktime(time.strptime(ti,'%Y,%m,%d-%H,%M,%S')))

t=time.time()
t=time.localtime(t)
print((time.strftime('%Y,%m,%d-%H,%M,%S',t)))