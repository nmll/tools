#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import random
import linecache


#<strong><span style="font-size:14px;">


'''
python2 creat_tag_1.py

'''

# 无重复生成一定范围内指定数目的随机数利用Python生成一定范围内指定数目的无重复随机数：
#mi为下限，ma为上限，num为数目，输出为num个数的列表
def random_without_same(mi, ma, num):
    temp = range(mi, ma)
    random.shuffle(temp)
    return temp[0:num] #</span>


#trackdatasetid=['0000.txt','0001.txt','0002.txt','0003.txt','0004.txt','0005.txt','0006.txt','0007.txt','0008.txt','0009.txt','0010.txt','0011.txt','0012.txt','0013.txt','0014.txt','0015.txt','0016.txt','0017.txt','0018.txt','0019.txt','0020.txt']
# 打开文件
id=[]

fi = open('./trainval.txt', "r")
fo = open('./train.txt', 'a')
fidata=fi.readlines()
num=len(fidata)
print(num)
id=random_without_same(1,num,num/2)#第几行
id.sort()
for n in id:
    data=linecache.getline(r'./trainval.txt',n)
    fo.write('%s' % data)


fi.close()
fo.close()
