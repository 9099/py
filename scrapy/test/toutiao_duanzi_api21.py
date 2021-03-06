#encoding:utf-8
import json
import multiprocessing
import random
import time

import pymongo
import requests


def init_database(collection):
    global coll
    conn = pymongo.MongoClient(host='115.159.98.124', port=27017)
    db = conn.get_database('toutiao')
    coll=db.get_collection(collection)
    # sel = 'ceshi%s'%(collection)
    # coll = db.create_collection(collection)

    # coll.insert_one({'x':2})
    return coll

def parse_url(category):
	t = time.time()
	t = int(t)
	tt = t - random.randint(80, 300)
	url ='http://www.toutiao.com/api/article/feed/?category={0}&widen=1&max_behot_time={1}&max_behot_time_tmp={2}&tadrequire=true&as=A145F928B8746C6&cp=598854061C060E1'.format(category,tt-random.randint(40,300),tt)
    # url = 'http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time={0}&last_refresh_sub_entrance_interval={1}&loc_mode=6&loc_time={2}&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123'.format(tt-random.randint(20,100), tt, tt-random.randint(400,900))
	return url

def parse(url,item,category,collection):
    req = requests.get(url)
    data1 = req.content
    data1 = json.loads(data1)
    data, label = item(data1)
    # print(data)
    if label==2:
        for d in data:
            try:
                d['content']=json.loads(d['content'])
            # d=dict(d)
                collection.insert_one(d)
            except:
                continue
    else:
        for d in data:
            try:
                collection.insert_one(d)
            except:
                continue
    end=time.time()
    if end-start>120:
        exit(0)
    parse(parse_url(category),item,category,collection)
    time.sleep(0.1)
    # parse(url,item)

def item(data1):
    data = data1['data']
    # next_time = data1['next']['max_behot_time']
    if data1.get('next'):
        label = 1  #不需要转化数组
    else:
        label =2
    return data, label

def main1(collection,category):
    collection=init_database(collection)
    parse(parse_url(category),item,category,collection)



if __name__== "__main__":
    # 热点
    # news_hot
    # 视频
    # video   ---------
    # 社会
    # news_society
    # 娱乐
    # news_entertainment ----------
    # 问答
    # question_and_answer
    # 图片
    # 组图
    # 科技
    # news_tech ----------
    # 汽车
    # news_car ----------
    # 体育
    # news_sport
    # 财经
    # news_finance ---------
    # 军事
    # news_military -------
    # 国际
    # news_world  ------
    # 段子
    # essay_joke ----
    # 趣图
    # image_funny
    # print(parse_url("image_funny"))

    # init_database("1")
    # url ='http://www.toutiao.com/api/article/feed/?category=essay_joke&widen=1&max_behot_time=1502106814&max_behot_time_tmp=1502106814&tadrequire=true&as=A145F928B8746C6&cp=598854061C060E1'
    # url='http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time=1492080290&last_refresh_sub_entrance_interval=1492080292&loc_mode=6&loc_time=1492079387&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123'
    start=time.time()
    # for i in range(20):
    # parse(url, item)
        # time.sleep(1)
    # main1('video','video')
    # s=init_database("ss")
    # s.insert_one({'x':2})


    pool = multiprocessing.Pool(8)
    arg=['video','news_entertainment','news_tech','news_car','news_finance','news_military','news_world','essay_joke']
    for i in range(8):
    # 	# mes="T%s"%(i)
        a=(arg[i])
        pool.apply_async(main1,args=(a,a))
    pool.close()
    pool.join()
