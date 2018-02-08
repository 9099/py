# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title  =scrapy.Field()
	url  =scrapy.Field()
	label  =scrapy.Field()
class TouTiaoDuanZiItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title  =scrapy.Field()
	url  =scrapy.Field()

class TouTiaoTechItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title  =scrapy.Field()
	url  =scrapy.Field()
	author  =scrapy.Field()
	author_url = scrapy.Field()
	author_avatar = scrapy.Field()
	comment_num = scrapy.Field()
	title_img = scrapy.Field()
	group_id = scrapy.Field()


class NextItem(scrapy.Item):
	next_url = scrapy.Field()
class AlimamaItem(scrapy.Item):
	title = scrapy.Field()
class MamaBaike(scrapy.Item):
	title=scrapy.Field()
	link=scrapy.Field()
class MamaQuanzi(scrapy.Item):
	louzhu_title=scrapy.Field()
	louzhu_author=scrapy.Field()
	louzhu_content=scrapy.Field()
	louzhu_place=scrapy.Field()

	lou_title=scrapy.Field()
	lou_author=scrapy.Field()
	lou_content=scrapy.Field()
	lou_place=scrapy.Field()

	louzhu=scrapy.Field()
	comment=scrapy.Field()


class Demo(scrapy.Item):
	image_urls=scrapy.Field()
	images=scrapy.Field()
	content = scrapy.Field()
	demo=scrapy.Field()
	title=scrapy.Field()
	image_paths=scrapy.Field()
class Jb51(scrapy.Item):
	image_urls=scrapy.Field()
	images=scrapy.Field()

	demo=scrapy.Field()
	title=scrapy.Field()
	image_paths=scrapy.Field()
class Qinzi(scrapy.Item):
	image_urls=scrapy.Field()
	images=scrapy.Field()
	demo=scrapy.Field()
	image_paths=scrapy.Field()