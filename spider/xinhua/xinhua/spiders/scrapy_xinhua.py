# -*- coding: utf-8 -*-
import scrapy

from xinhua.items import XinhuaItem
import re

class ScrapyXinhuaSpider(scrapy.Spider):
    name = 'scrapy_xinhua'
    allowed_domains = ['xinhuanet.com']
    start_urls = ['http://www.xinhuanet.com/']

    def parse(self, response):
        def getdomain(url):
            proto, rest = urllib.splittype(url)
            host, rest = urllib.splithost(rest)
            return "http://"+host
        sel=scrapy.Selector(response)
        links_in_a_page=sel.xpath('//a[@href]')

        for link_sel in links_in_a_page:
            item=XinhuaItem()
            link=str(link_sel.re('href="(.*?)"')[0])


            if link:
                if not link.startswith('http'):
                    link=response.url+link
                    #link=getdomain(response.url)+link

                

                yield scrapy.Request(link,callback=self.parse)

                p1=re.compile(r'.*\d{4}-\d{2}/\d{2}.*')
                if re.match(p1,link):
                    print ("Y: "+link)
                    item['link']=link
                    yield item
                else:
                    print ("F: "+link)

