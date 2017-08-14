# -*- coding: utf-8 -*-
import scrapy
from sohu.items import SohuItem
import urllib
import re


class ScrapySohuSpider(scrapy.Spider):
    name = 'scrapy_sohu'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    def parse(self, response):
        def getdomain(url):
            #proto,rest=urllib.splittype(url)
            #host,rest=urllib.splithost(rest)
            return "http:"

        sel =  scrapy.Selector(response)
        links_in_a_page=sel.xpath('//a[@href]')

        for link_sel in links_in_a_page:
            item=SohuItem()
            link=str(link_sel.re('href="(.*?)"')[0])

            if link:
                if not link.startswith('http'):
                    link=getdomain(response.url)+link

                yield scrapy.Request(link,callback=self.parse)

                p1=re.compile(r'.*/a/.*')
                p2=re.compile(r'.*#comment_area$')
                p3=re.compile(r'.*news.sohu.com.*s?html?$')

				

                if (re.match(p3,link) or re.match(p1,link)) and (not re.match(p2,link)):
                    #print ('T: '+link)
                    item['link']=link
                    yield item
                else:
                    pass
                    #print ('F: '+link)
