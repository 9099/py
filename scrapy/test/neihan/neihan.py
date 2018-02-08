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
    db = conn.get_database('neihan')
    coll=db.get_collection(collection)
    # sel = 'ceshi%s'%(collection)
    # coll = db.create_collection(collection)

    # coll.insert_one({'x':2})
    return coll

def parse_url(category):
    t = time.time()
    t = t-random.randint(40,600)
    st=int(time.time()*1000)
    t = int(t)
    tt = st - random.randint(80, 300)
    url ='http://iu.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type={0}&message_cursor=-1&am_longitude=110&am_latitude=120&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time={1}&count=30&min_time={2}&screen_width=1450&do00le_col_mode=0&iid=3216590132&device_id=32613520945&ac=wifi&channel=360&aid=7&app_name=joke_essay&version_code=612&version_name=6.1.2&device_platform=android&ssmix=a&device_type=sansung&device_brand=xiaomi&os_api=28&os_version=6.10.1&uuid=326135942187625&openudid=3dg6s95rhg2a3dg5&manifest_version_code=612&resolution=1450*2800&dpi=620&update_version_code=6120'.format(category,tt,t+random.randint(40,300))
    # url = 'http://is.snssdk.com/api/news/feed/v51/?concern_id=12345678228934679042&refer=1&count=20&min_behot_time={0}&last_refresh_sub_entrance_interval={1}&loc_mode=6&loc_time={2}&latitude=28.687511709859&longitude=116.02067822305&city=%E5%8D%97%E6%98%8C%E5%B8%82&tt_from=pull&lac=31176&cid=123456789&cp=5183e0f15e6a4q1&iid=0123456789&device_id=12345678952&ac=wifi&channel=oppo-cpa&aid=13&app_name=news_article&version_code=607&version_name=6.0.7&device_platform=ios&ab_version=116031%2C112577%2C101786%2C117787%2C114037%2C101533%2C118766%2C110341%2C113607%2C118273%2C114108%2C106784%2C113608%2C101558%2C105475%2C118213%2C117714%2C105610%2C118751%2C104321%2C118607%2C117725%2C112578%2C115570%2C118602%2C118850%2C115776%2C116615%2C118660%2C31650%2C118530%2C118976%2C118216%2C114338%2C118846&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=94563%2C102749&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=XIAOMI&device_brand=Google&language=zh&os_api=23&os_version=6.0&openudid=123456789d36d6z6&manifest_version_code=607&resolution=1080*1821&dpi=440&update_version_code=6075&_rticket=123456789123'.format(tt-random.randint(20,100), tt, tt-random.randint(400,900))
    return url

def parse(url,category,collection):
    req = requests.get(url)
    data1 = req.content
    # print(data1)
    data1 = json.loads(data1)
    data=data1['data']['data']

    if data:
        # print(data)
        for d in data:
            if d.get('ad'):
                continue
            try:
                collection.insert_one(d)
            except:
                continue
    else:
        pass

    end=time.time()
    if end-start>57:
        exit(0)
    time.sleep(0.1)
    parse(parse_url(category),category,collection)

    # parse(url,item)



def main1(collection,category):
    collect=init_database(collection)
    parse(parse_url(category),category,collect)



if __name__== "__main__":

    start=time.time()
    #
    #
    pool = multiprocessing.Pool(4)
    arg=['-101','-102','-103','-104']
    arg1=['tuijian','duanzi','pic','video']

    # for i in range(4):
    #     a1=arg1[i]
    #     a=arg[i]
    #     pool.apply_async(main1,args=(a1,a))
    #
    # pool.close()
    # pool.join()
    main1(arg1[0],arg[0])
