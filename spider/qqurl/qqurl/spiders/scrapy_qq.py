# -*- coding: utf-8 -*-
import scrapy
from qqurl.items import QqurlItem
import re

import urllib
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class ScrapyQqSpider(scrapy.Spider):
    name = 'scrapy_qq'
    allowed_domains = ['news.qq.com']
    start_urls = ['http://news.qq.com/']
    


    def parse(self, response):
        def getdomain(url):
            proto, rest = urllib.splittype(url)
            host, rest = urllib.splithost(rest)
            return "http://"+host

        sel=scrapy.Selector(response)
        links_in_a_page = sel.xpath('//a[@href]')

        for link_sel in links_in_a_page:
            item=QqurlItem()
            link=str(link_sel.re('href="(.*?)"')[0])
            
            if link:
                if not link.startswith('http'):
                    if link.startswith('javascript'):
                        continue
                    if link.startswith('//support'):
                        continue
                    link=getdomain(response.url)+link


                if  re.match('.*comment.*',link):
					continue


                yield scrapy.Request(link,callback=self.parse)
                if not re.match('.*comment.*',link):
                    if re.match('^http.*qq.com.*\.s?html?$',link):
                        item['link']=link
                        yield item
