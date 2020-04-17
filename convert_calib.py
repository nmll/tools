#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import random


trackdatasetid=['0000.txt','0001.txt','0002.txt','0003.txt','0004.txt','0005.txt','0006.txt','0007.txt','0008.txt','0009.txt','0010.txt','0011.txt','0012.txt','0013.txt','0014.txt','0015.txt','0016.txt','0017.txt','0018.txt','0019.txt','0020.txt']
# 打开文件
aa=[]
com=[]
fi = open('./trainval.txt', "r")
fcom = open('./train.txt', "r")
fo = open('./val.txt', 'a')
aa=fi.readlines()
com=fcom.readlines()

for n in aa:
    id=True
    for x in com:
        if n == x:
            id = False
            continue

    if id:
        fo.write('%s'%n)



fi.close()
fo.close()
fcom.close()