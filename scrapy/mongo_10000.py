# -*- coding:utf-8 -*-
import time
import sys
import json
import pymongo
# data = sys.argv[1]
# print(type(data))
# print((data))
js =json.loads('{"x":"5"}');
# print(type(js))
# print((js))

start = time.clock()
for i in range(10000):
    js =json.loads('{"_id":ObjectId("59842c8195eafe23ead504c8"),"display_time":1501832268,"group":{"text":"不管与谁相处，信任，才能拉近距离；真诚，才能走进心里！不管世界怎么变，社会怎么乱，正直，永远最可贵，善良，永远不过期！一个真诚的人，走到哪里都会有人喜欢。因为说话认真，做事用心，为人诚恳。一颗善良的心，和谁相伴都能长远。因为懂体谅，懂包容，懂尊重。人这一生，好名声，是用有情有义赚来的；好感情，是用实心实意换来的；好人品，是用一辈子去打造的！做人，一定要以真诚为先；心灵，一定要以善良为本！","neihan_hot_start_time":"00-00-00","dislike_reason":[{"type":1,"id":410,"title":"语录"},{"type":2,"id":28,"title":"吧:花美男"},{"type":4,"id":0,"title":"内容重复"},{"type":3,"id":1933888583,"title":"作者:懒得换了"}],"create_time":1501655022,"id":NumberLong(64878742342),"favorite_count":4,"user_bury":0,"user_favorite":0,"share_type":0,"max_screen_width_percent":0.6,"is_can_share":1,"comment_count":2,"share_url":"http://m.neihanshequ.com/share/group/64878742342/?iid=3216590132&app=joke_essay","label":4,"content":"不管与谁相处，信任，才能拉近距离；真诚，才能走进心里！不管世界怎么变，社会怎么乱，正直，永远最可贵，善良，永远不过期！一个真诚的人，走到哪里都会有人喜欢。因为说话认真，做事用心，为人诚恳。一颗善良的心，和谁相伴都能长远。因为懂体谅，懂包容，懂尊重。人这一生，好名声，是用有情有义赚来的；好感情，是用实心实意换来的；好人品，是用一辈子去打造的！做人，一定要以真诚为先；心灵，一定要以善良为本！","category_type":2,"id_str":"64878742342","media_type":1,"share_count":9,"type":3,"category_id":28,"status":102,"has_comments":0,"large_image":{"url_list":[{"url":"http://p1.pstatp.com/w640/337800024504e5153b12.webp"},{"url":"http://pb3.pstatp.com/w640/337800024504e5153b12.webp"},{"url":"http://pb9.pstatp.com/w640/337800024504e5153b12.webp"}],"uri":"w640/337800024504e5153b12","height":900,"width":640,"r_height":900,"r_width":640},"go_detail_count":93,"neihan_hot_link":{},"status_desc":"已发表，粉丝第一时间可见","quick_comment":false,"user":{"user_id":1933888583,"name":"懒得换了","followings":0,"is_pro_user":false,"ugc_count":176,"avatar_url":"http://p1.pstatp.com/medium/216f0004ee83d284ed80","followers":175,"is_following":false,"user_verified":false},"neihan_hot_end_time":"00-00-00","is_personal_show":false,"user_digg":0,"online_time":1501655022,"category_name":"花美男","group_id":NumberLong(64878742342),"bury_count":5,"is_anonymous":false,"repin_count":4,"min_screen_width_percent":0.167,"is_neihan_hot":false,"digg_count":107,"has_hot_comments":0,"allow_dislike":true,"image_status":1,"user_repin":0,"activity":{},"category_visible":true,"middle_image":{"url_list":[{"url":"http://p1.pstatp.com/w480/337800024504e5153b12.webp"},{"url":"http://pb3.pstatp.com/w480/337800024504e5153b12.webp"},{"url":"http://pb9.pstatp.com/w480/337800024504e5153b12.webp"}],"uri":"w480/337800024504e5153b12","height":900,"width":640,"r_height":675,"r_width":480},"display_type":0},"online_time":1501832268,"comments":[],"type":1}');
    conn = pymongo.MongoClient(host='127.0.0.1',port=27017)
    db = conn.demo
    coll = db.test7
    coll.insert_one(js)
    # print(js)
end = time.clock()
print(end-start)