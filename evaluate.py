#coding=utf-8
import re
import sys
import os

str1 = []
str2 = []
str_dump = []
fa = open("x/1.txt", 'r')
fb = open("y/1.txt", 'r')
fc = open("diee.txt", 'w+')

# 将A.txt的内容逐行读到str1中
count_gt=0
for line in fa.readlines():
    count_gt=count_gt+1
    str1.append(line.replace("\n", ''))


# 将B.txt中的内容逐行读到str2中
for line in fb.readlines():
    str2.append(line.replace("\n", ''))

# 将两个文件中重复的行，添加到str_dump中
for i in str1:
    if i in str2:
        str_dump.append(i)




for i in str_dump:
    if i in str1:
        str1.remove(i)
for i in str_dump:
    if i in str2:
	    str2.remove(i)

print 'miss_data'+str(str1)
print "============"
print 'redundancy_data'+str(str2)

fa.close()
fb.close()
fc.close()
