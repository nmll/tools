#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
转换数据集雷达和calib数据和camera,并生成trainval文件标签

'''


import os
import shutil
trackdirid=['0000','0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011',
            '0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022',
            '0023','0024','0025','0026','0027','0028']


trackdatasetid=['0000.txt','0001.txt','0002.txt','0003.txt','0004.txt','0005.txt','0006.txt','0007.txt','0008.txt','0009.txt','0010.txt','0011.txt','0012.txt','0013.txt','0014.txt','0015.txt','0016.txt','0017.txt','0018.txt','0019.txt','0020.txt',
                '0021.txt','0022.txt','0023.txt','0024.txt','0025.txt','0026.txt','0027.txt','0028.txt',]

path = os.getcwd()    #获取当前路径
"""
####### move testing lidar
outpath = os.path.join(path, 'object_tracking/testing/velodyne')
for i in range(29):
    count = 0
    n=000000
    for root, dirs, files in os.walk(path+'/object/testing/velodyne/%s'%trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        origin_dir = os.path.join(path, 'object/testing/velodyne')
        origin_path = r'%s/%s/%s.bin' % (origin_dir,trackdirid[i],"{:06d}".format(n))  # 原始文件完整目录
        new_file_name = r'%s/%s-%s.bin' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        shutil.copyfile(origin_path, new_file_name)
    #     fo.write('%6d\n'%n)
    #     #n+=random.randint(1, 6)  # 依次读取每行
        n+=1

####### move training lidar
outpath = os.path.join(path,'object_tracking/training/velodyne')
for i in range(21):
    count = 0
    n = 000000
    for root, dirs, files in os.walk(path + '/object/training/velodyne/%s' % trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        new_file_name = r'%s/%s-%s.bin' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        origin_dir = os.path.join(path, 'object/training/velodyne')
        #origin_dir=path+'object/training/velodyne/%s/%s' % trackdirid[i],"{:06d}".format(n)
        origin_path = r'%s/%s/%s.bin' % (origin_dir,trackdirid[i],"{:06d}".format(n))  # 原始文件完整目录
        shutil.copyfile(origin_path, new_file_name)
        #     fo.write('%6d\n'%n)
        #     #n+=random.randint(1, 6)  # 依次读取每行
        n+= 1
"""
# ####### move training calib
# outpath = os.path.join(path,'object_tracking/training/calib')
# for i in range(21):
#     count = 0
#     n = 000000
#     for root, dirs, files in os.walk(path + '/object/training/velodyne/%s' % trackdirid[i]):  # 遍历统计
#         for each in files:
#             count += 1  # 统计文件夹下文件个数
#     while n < count:
#         new_file_name = r'%s/%s-%s.txt' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
#         origin_dir = os.path.join(path, 'object/training/calib')
#         #origin_dir=path+'object/training/velodyne/%s/%s' % trackdirid[i],"{:06d}".format(n)
#         origin_path = r'%s/%s.txt' % (origin_dir,trackdirid[i])  # 原始文件完整目录
#         shutil.copyfile(origin_path, new_file_name)
#         #     fo.write('%6d\n'%n)
#         #     #n+=random.randint(1, 6)  # 依次读取每行
#         n+= 1

# ####### move testing calib
# outpath = os.path.join(path, 'object_tracking/testing/calib')
# for i in range(29):
#     count = 0
#     n=000000
#     for root, dirs, files in os.walk(path+'/object/testing/velodyne/%s'%trackdirid[i]):  # 遍历统计
#         for each in files:
#             count += 1  # 统计文件夹下文件个数
#     while n < count:
#         origin_dir = os.path.join(path, 'object/testing/calib')
#         origin_path = r'%s/%s.txt' % (origin_dir,trackdirid[i])  # 原始文件完整目录
#         new_file_name = r'%s/%s-%s.txt' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
#         shutil.copyfile(origin_path, new_file_name)
#     #     fo.write('%6d\n'%n)
#     #     #n+=random.randint(1, 6)  # 依次读取每行
#         n+=1
####### move training camera
fo = open('./trainval.txt', 'a')
outpath = os.path.join(path,'object_tracking/training/image_2')
for i in range(21):
    count = 0
    n = 000000
    for root, dirs, files in os.walk(path + '/object/training/image_02/%s' % trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        new_file_name = r'%s/%s-%s.png' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        origin_dir = os.path.join(path, 'object/training/image_02')
        #origin_dir=path+'object/training/velodyne/%s/%s' % trackdirid[i],"{:06d}".format(n)
        origin_path = r'%s/%s/%s.png' % (origin_dir,trackdirid[i],"{:06d}".format(n))  # 原始文件完整目录
        shutil.copyfile(origin_path, new_file_name)

        fo.write('%s-%s\n' % (trackdirid[i],"{:06d}".format(n)))
        #     fo.write('%6d\n'%n)
        #     #n+=random.randint(1, 6)  # 依次读取每行
        n+= 1

