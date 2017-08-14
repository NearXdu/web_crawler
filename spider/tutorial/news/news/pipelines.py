# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('tencent_news.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class NewsPipeline(object):
   def __init__(self):
        dbargs = dict(
             host = '127.0.0.1',
             db = 'test',
             user = 'root',
             passwd = '123456',
             cursorclass = MySQLdb.cursors.DictCursor,
             charset = 'utf8',
             use_unicode = True
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
   def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
   def insert_into_table(self,conn,item):
        conn.execute('insert into tencent_news(content, title) values(%s,%s)', (
                item['content'][0],
                item['title'][0])
                )

