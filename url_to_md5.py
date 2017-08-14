import hashlib


## 1. read urls from file
urls=[]
with open('urls.txt') as f:
    line = f.readline()
    while line:
        urls.append(line)
        line = f.readline()
print (len(urls))

## 2.define a function
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()


md5s=[]
for url in urls:
    md5s.append(md5(url.strip()))

f=open('md5.txt','w')
for i in md5s:
    print i
    f.write(i)
    f.write('\n')
f.close()

 
    


