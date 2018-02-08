# -*- coding:utf-8 -*-


import pymysql
import requests
import json
import sys

import time

##############################

for i in range(10):
    kaiyan = requests.get("http://baobab.kaiyanapp.com/api/v4/discovery/hot")

    data = kaiyan.content
    data.encode('utf-8')
    jdata = json.loads(data)
    # print(jdata["author"])
    # while jdata["nextPageUrl"]:

    data_list = jdata['itemList']
    for it in data_list:

        if it['type']=="video":

            it_data = it['data']
            # print(it_data["author"]['name'])
            title=str(it_data["title"])
            description=str(it_data["description"])
            category=str(it_data["category"])
            playUrl=str(it_data["playUrl"])
            duration=str(it_data["duration"])
            date=str(it_data["date"])[:-3]
            if  it_data["author"] == None:
                author_name=""
                author_description=''
            else:
                author_name=str(it_data["author"]['name'])
                author_description=str(it_data["author"]["description"])

            cover_feed=str(it_data["cover"]["feed"])
            cover_detail=str(it_data["cover"]["detail"])
            cover_blurred=str(it_data["cover"]["blurred"])
            releaseTime=str(it_data["releaseTime"])[:-3]
            kaiyan_id=str(it_data["id"])
            if it_data["playInfo"] ==None or len(it_data["playInfo"])==0:
                url_nomal=""
            else:
                url_nomal=str(it_data["playInfo"][0]["url"])

            ####################################################数据库插入操作
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='caiji_kaiyan', charset='utf8')
            cursor = conn.cursor()
            cursor.execute('insert into caiji_video(title,description,category,playUrl,duration,date,author_name,author_description,cover_feed,cover_detail,cover_blurred,releaseTime,kaiyan_id,url_nomal) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,(title,description,category,playUrl,duration,date,author_name,author_description,cover_feed,cover_detail,cover_blurred,releaseTime,kaiyan_id,url_nomal))
            # cursor.execute('insert into caiji_video(title) values(%s)' ,("sd"))

            conn.commit()
            cursor.close()
            conn.close()
        # time.sleep(0.3)
        # print(title,"++++++",description,"++++++",category,"++++++",playUrl,"++++++",duration,"++++++",date,"++++++",author_name,"++++++",author_description,"++++++",cover_feed,"++++++",cover_detail,"++++++",cover_blurred,"++++++",releaseTime,"++++++",kaiyan_id,"++++++",url_nomal)
######################################################
#############################
