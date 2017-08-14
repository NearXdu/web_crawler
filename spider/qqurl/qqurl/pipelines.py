# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import re

class QqurlPipeline(object):
    def __init__(self):
        self.file=open('qqurl.jl','w')
        self.seen=set()
    def process_item(self, item, spider):
        if not re.match('.*comment.*',item['link']):
            if re.match('^http.*qq.com.*\.s?html?$',item['link']):
                if item['link'] in self.seen:
                    raise DropItem('Duplicate link %s' % item['link'])
                self.seen.add(item['link'])
                line = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file.write(line)
                return item
