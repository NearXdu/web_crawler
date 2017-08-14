# -*- coding: UTF-8 -*-

import urllib2
import json
import hashlib
from collections import OrderedDict
import io
import re
## 0. md5 function
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

def filter_h5(str):
    return re.sub(r'</?\w+[^>]*>','',str)

## 1. set proxy
proxy = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

## 2.url to md5
urls=[]
with open('urls.txt') as f:
    line = f.readline()
    while line:
        urls.append(line)
        line = f.readline()
md5s=OrderedDict()
for url in urls:
    md5s[url]=md5(url.strip())


## 3.iteration
i = 0;
path="./ground_truth/"
for url in md5s:
    i=i+1
    raw_id=md5s[url]
#api

    strHtml = urllib2.urlopen(str(api)).read()
    raw_json=json.loads(strHtml)
    if raw_json['response']['code'] is -1:
	    continue;
    else:
        data_json=raw_json['data']
        filename=path+str(i)+"_running"+".txt"
        raw_content= data_json[u'文章内容']
        content=filter_h5(raw_content)
        if content:
            f=io.open(filename, 'wt',encoding='utf8')
            f.write(url+'\n')
            f.write(content)
            print ('write '+filename)


