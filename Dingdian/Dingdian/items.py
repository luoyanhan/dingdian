# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    novelurl = scrapy.Field()
    status = scrapy.Field()
    wordnumber = scrapy.Field()
    category = scrapy.Field()
    name_id = scrapy.Field()

class DcontentItem(scrapy.Item):
    id_name = scrapy.Field()
    chaptercontent = scrapy.Field()
    num = scrapy.Field()
    chapterurl = scrapy.Field()
    chaptername = scrapy.Field()
