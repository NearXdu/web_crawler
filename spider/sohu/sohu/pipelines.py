# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pandas as pd
import redis

import mysql.connector
import json
import re
redis_db = redis.Redis(host="127.0.0.1", port=6379, db=4, password="123456")
redis_data_dict = "f_uuids"
class SohuPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(user = 'zx', password='123456', database='sohudb', charset='utf8')    

        redis_db.flushdb()
        if redis_db.hlen(redis_data_dict) == 0:
            sql = "SELECT url FROM sohuurl;"
            df = pd.read_sql(sql, self.conn)
            for url in df['url'].get_values():
                redis_db.hset(redis_data_dict, url, 0) 


    def process_item(self, item, spider):
        if redis_db.hexists(redis_data_dict, item['link']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
#            print item['link']

            cur=self.conn.cursor()
            add_url = """insert into sohuurl(url) VALUES (%s)"""
            data_url=(str(item['link']),)
            cur.execute(add_url,data_url)
            self.conn.commit()
            cur.close()
            return item
