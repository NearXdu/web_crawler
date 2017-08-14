import scrapy
from news.items import NewsItem

class Tencent(scrapy.Spider):
    name='tencent_news'
    allowed_domains=['qq.com']

    f=open('a.txt','r')
    start_urls=[]

    while True:
        line=f.readline()
        if line:
            line=line.strip().replace("['","").replace("']","")
            p=line.rfind('.')
            filename=line[0:p]
            print "the url is %s"%line
            start_urls.append(line)
        else:
            break
    f.close()


    def parse(self,response):
        item=NewsItem()
        item['content']=response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
        item['title'] = response.xpath('//div[@class="hd"]/h1/text()').extract()
        yield item



