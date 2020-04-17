#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''

kittidataet testing 计算image下文件个数输出生成假的testinglabel文件
'''



import os
import random
trackdirid=['0000','0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011',
            '0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022',
            '0023','0024','0025','0026','0027','0028']


trackdatasetid=['0000.txt','0001.txt','0002.txt','0003.txt','0004.txt','0005.txt','0006.txt','0007.txt','0008.txt','0009.txt','0010.txt','0011.txt','0012.txt','0013.txt','0014.txt','0015.txt','0016.txt','0017.txt','0018.txt','0019.txt','0020.txt',
                '0021.txt','0022.txt','0023.txt','0024.txt','0025.txt','0026.txt','0027.txt','0028.txt',]
# 打开文件
aa=[]
path = os.getcwd()    #获取当前路径
count = 0
for i in range(29):
    #num=len([x for x in os.listdir(os.path.dirname('/raid/workspace/liyao/kittidataset/object/testing/image_02/%s/'%trackdirid[i])) if os.path.isfile(x)])
    count = 0
    fo = open('./label_02/' + '%s'%trackdatasetid[i], 'a')
    n=000000

    for root, dirs, files in os.walk(path+'/image_02/%s'%trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
     # 输出结果
    print(count)
    while n < count:

        fo.write('%6d\n'%n)
        #n+=random.randint(1, 6)  # 依次读取每行
        n+=1
fo.close()
