#encoding:utf-8
import random

import jieba
import jieba.posseg
import csv
import pypinyin


def cut():
	for i in open('货币战争1.txt', 'r'):
		s = (jieba.cut(i))
		yield s

def filt(x):
	if len(x)>8:
		return False
	elif len(x.strip())<=1:
		return False
	else:
		return True
# se=cut()
# with open('list.csv','a') as f:
#
# 	for i in se:
# 		res=list(filter(filt,list(se.__next__())))
# 		res=pypinyin.lazy_pinyin(res)
# 		res=','.join(res)+'\n'
# 		f.writelines(res)
# import linecache
# buff=[]
# for i in range(70):
# 	rand=random.randrange(0,4000)
# 	buff+=(linecache.getline('list.csv',rand).strip().split(','))
# print(buff)
s='XuzhouusedtobeintheterritoryofChuStateintheQinandHanDynasties.Itwasthecapital'

print(list(jieba.cut(s)))