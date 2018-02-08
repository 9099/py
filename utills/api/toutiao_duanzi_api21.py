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
	db = conn.get_database('zuiyou')
	coll=db.get_collection(collection)
	# sel = 'ceshi%s'%(collection)
	# coll = db.create_collection(collection)

	# coll.insert_one({'x':2})
	return coll
def header2dict(header):
	header = header.strip().split('\n')
	buff=[]
	for i in header:
		buff.append(i.strip())
	buff = {x.split(':', maxsplit=1)[0]: x.split(':', maxsplit=1)[1].strip() for x in buff}
	return buff
def parse_content():
	head = '''
	Host: tbapi.ixiaochuan.cn
	Content-Length: 278
	Content-Type: text/plain; charset=utf-8
	Connection: Keep-Alive
	Cookie: aliyungf_tc=AQAAAI6DGU10ZAoAyR9EMVz90Z/HBLC8
	Cookie2: $Version=1
	Accept-Encoding: gzip
	ZYP: mid=34187505

	'''
	head = header2dict(head)
	t=int(time.time()*1000)-random.randrange(4000,99999)
	data = '{"offset":0,"filter":"video","tab":"rec","direction":"down","auto":0,"h_av":"3.6.4","h_dt":0,"h_os":22,"h_model":"m3 note","h_did":"862143030414424_a4:44:d1","h_nt":1,"h_m":34187505,"h_ch":"meizu","h_ts":%s,"token":"TaK2NAplOdT3n8QV5PPjA3KEABE3dG8TbegonYfqFVDpXqYo="}'%(t)

	res = requests.post('http://tbapi.ixiaochuan.cn/index/recommend?sign=6bf82b6962e7af7858cce3058c5d544e', data=data,
						headers=head)
	return res.json()

def parse(collection):
	data=parse_content()
	data=data['data']['list']
	print(data)
	if len(data)>300:

		for d in data:
			try:

			# d=dict(d)
				collection.insert_one(d)
			except:
				continue
	else:
		pass
	end=time.time()
	if end-start>20:
		exit(0)
	time.sleep(1)
	parse(collection)
	# parse(url,item)


def main1(collection):
	collect=init_database(collection)
	parse(collect)



if __name__== "__main__":
	start = time.time()
	main1('video')

