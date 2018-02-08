# -*- coding:utf-8 -*-


import pymysql
import requests
import json
import pymongo
import sys

import time

##############################
# http://iu.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-101&message_cursor=-1&am_longitude=110&am_latitude=120&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1463225362314&count=30&min_time=1465232121&screen_width=1450&do00le_col_mode=0&iid=3216590132&device_id=32613520945&ac=wifi&channel=360&aid=7&app_name=joke_essay&version_code=612&version_name=6.1.2&device_platform=android&ssmix=a&device_type=sansung&device_brand=xiaomi&os_api=28&os_version=6.10.1&uuid=326135942187625&openudid=3dg6s95rhg2a3dg5&manifest_version_code=612&resolution=1450*2800&dpi=620&update_version_code=6120

for i in range(10):
    kaiyan = requests.get("http://iu.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-101&message_cursor=-1&am_longitude=110&am_latitude=120&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1463225362314&count=30&min_time=1465232121&screen_width=1450&do00le_col_mode=0&iid=3216590132&device_id=32613520945&ac=wifi&channel=360&aid=7&app_name=joke_essay&version_code=612&version_name=6.1.2&device_platform=android&ssmix=a&device_type=sansung&device_brand=xiaomi&os_api=28&os_version=6.10.1&uuid=326135942187625&openudid=3dg6s95rhg2a3dg5&manifest_version_code=612&resolution=1450*2800&dpi=620&update_version_code=6120")

    data = kaiyan.content
    data.encode('utf-8')
    jdata = json.loads(data)
    # print(jdata["author"])
    # while jdata["nextPageUrl"]:
    conn = pymongo.MongoClient(host='127.0.0.1',port=27017)
    db = conn.demo
    coll = db.test1
    result=coll.insert(jdata)
    # data_list = jdata['data']['data']
    # for it in data_list:

        # if it['type']=="video":
        #
        #     it_data = it['data']
        #     # print(it_data["author"]['name'])
        #     title=str(it_data["title"])
        #     description=str(it_data["description"])
        #     category=str(it_data["category"])
        #     playUrl=str(it_data["playUrl"])
        #     duration=str(it_data["duration"])
        #     date=str(it_data["date"])[:-3]
        #     if  it_data["author"] == None:
        #         author_name=""
        #         author_description=''
        #     else:
        #         author_name=str(it_data["author"]['name'])
        #         author_description=str(it_data["author"]["description"])
        #
        #     cover_feed=str(it_data["cover"]["feed"])
        #     cover_detail=str(it_data["cover"]["detail"])
        #     cover_blurred=str(it_data["cover"]["blurred"])
        #     releaseTime=str(it_data["releaseTime"])[:-3]
        #     kaiyan_id=str(it_data["id"])
        #     if it_data["playInfo"] ==None or len(it_data["playInfo"])==0:
        #         url_nomal=""
        #     else:
        #         url_nomal=str(it_data["playInfo"][0]["url"])
        #
        #     ####################################################数据库插入操作
        #     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='caiji_kaiyan', charset='utf8')
        #     cursor = conn.cursor()
        #     cursor.execute('insert into caiji_video(title,description,category,playUrl,duration,date,author_name,author_description,cover_feed,cover_detail,cover_blurred,releaseTime,kaiyan_id,url_nomal) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,(title,description,category,playUrl,duration,date,author_name,author_description,cover_feed,cover_detail,cover_blurred,releaseTime,kaiyan_id,url_nomal))
        #     # cursor.execute('insert into caiji_video(title) values(%s)' ,("sd"))
        #
        #     conn.commit()
        #     cursor.close()
        #     conn.close()
        # time.sleep(0.3)
        # print(title,"++++++",description,"++++++",category,"++++++",playUrl,"++++++",duration,"++++++",date,"++++++",author_name,"++++++",author_description,"++++++",cover_feed,"++++++",cover_detail,"++++++",cover_blurred,"++++++",releaseTime,"++++++",kaiyan_id,"++++++",url_nomal)
######################################################
#############################
        # conn = pymongo.MongoClient(host='127.0.0.1',port=27017)
        # db = conn.demo
        # coll = db.test
        # result=coll.insert(it)
        # print(result)