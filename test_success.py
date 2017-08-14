import newspaper
import io
from newspaper import Article


## 1. read urls from file
urls=[]
with open('urls.txt') as f:
    line = f.readline()
    while line:
        urls.append(line)
        line = f.readline()
## test
print (len(urls))
	


## 2. extract content from web page
i=1
for url in urls:
    print ("number: %d url: %s"%(i,url))
    a=Article(url.strip(),language='zh')
    a.download()
    a.parse() 
    content=a.text
## 3. write content to file system
    path="./result/"
    filename=path+str(i)+"_nlp"+".txt"
    with io.open(filename, 'wt',encoding='utf8') as f:
	    f.write(content)
    i=i+1
