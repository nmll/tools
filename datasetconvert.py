#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
把kittidataset从tracking数据集转换成detection数据集的格式，包括雷达和calib数据和camera,并生成trainval文件标签
在object_tracking同级的路径下，原始文件名为object
转化kittitracking label成detection的label格式
'''

from collections import defaultdict#可以创建字典一个key多个value
import os
import shutil
import logging
trackdirid=['0000','0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011',
            '0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022',
            '0023','0024','0025','0026','0027','0028']


trackdatasetid=['0000.txt','0001.txt','0002.txt','0003.txt','0004.txt','0005.txt','0006.txt','0007.txt','0008.txt','0009.txt','0010.txt','0011.txt','0012.txt','0013.txt','0014.txt','0015.txt','0016.txt','0017.txt','0018.txt','0019.txt','0020.txt',
                '0021.txt','0022.txt','0023.txt','0024.txt','0025.txt','0026.txt','0027.txt','0028.txt',]

path = os.getcwd()    #获取当前路径
#path='D:/xunleixiazai/' #windows 下  need to be modified to your path
os.makedirs(path+'/object_tracking/testing/velodyne')
os.makedirs(path+'/object_tracking/training/velodyne')
os.makedirs(path+'/object_tracking/testing/image_2')
os.makedirs(path+'/object_tracking/training/image_2')
os.makedirs(path+'/object_tracking/training/calib')
os.makedirs(path+'/object_tracking/testing/calib')

os.makedirs(path+'/object_tracking/training/label_2')


logging.basicConfig(level=logging.INFO)
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
logging.info('the last group convert %d testing velodyne' % count)

####### move training lidar
outpath = os.path.join(path,'object_tracking/training/velodyne')
#补充原始文件缺少的帧
origin_dir = os.path.join(path, 'object/training/velodyne')
shutil.copyfile(origin_dir+r'/0001/000176.bin', origin_dir+r'/0001/000177.bin')
shutil.copyfile(origin_dir+r'/0001/000176.bin', origin_dir+r'/0001/000178.bin')
shutil.copyfile(origin_dir+r'/0001/000181.bin', origin_dir+r'/0001/000180.bin')
shutil.copyfile(origin_dir+r'/0001/000181.bin', origin_dir+r'/0001/000179.bin')

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

logging.info('the last group convert %d training velodyne' % count)

####### move testing cmera
outpath = os.path.join(path, 'object_tracking/testing/image_2')
for i in range(29):
    count = 0
    n=000000
    for root, dirs, files in os.walk(path+'/object/testing/image_02/%s'%trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        origin_dir = os.path.join(path, 'object/testing/image_02')
        origin_path = r'%s/%s/%s.png' % (origin_dir,trackdirid[i],"{:06d}".format(n))  # 原始文件完整目录
        new_file_name = r'%s/%s-%s.png' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        shutil.copyfile(origin_path, new_file_name)
    #     fo.write('%6d\n'%n)
    #     #n+=random.randint(1, 6)  # 依次读取每行
        n+=1
logging.info('the last group convert %d testing camera' % count)

####### move training camera and produce trainval.txt
fo = open('./trainval.txt', 'w')
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

logging.info('the last group convert %d training camera' % count)


####### move training calib
outpath = os.path.join(path,'object_tracking/training/calib')
for i in range(21):
    count = 0
    n = 000000
    for root, dirs, files in os.walk(path + '/object/training/image_02/%s' % trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        new_file_name = r'%s/%s-%s.txt' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        origin_dir = os.path.join(path, 'object/training/calib')
        #origin_dir=path+'object/training/velodyne/%s/%s' % trackdirid[i],"{:06d}".format(n)
        origin_path = r'%s/%s.txt' % (origin_dir,trackdirid[i])  # 原始文件完整目录
        shutil.copyfile(origin_path, new_file_name)

        #     fo.write('%6d\n'%n)
        #     #n+=random.randint(1, 6)  # 依次读取每行
        n+= 1


logging.info('the last group convert %d training calib' % count)



####### move testing calib
outpath = os.path.join(path, 'object_tracking/testing/calib')
for i in range(29):
    count = 0
    n=000000
    for root, dirs, files in os.walk(path+'/object/testing/image_02/%s'%trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    while n < count:
        origin_dir = os.path.join(path, 'object/testing/calib')
        origin_path = r'%s/%s.txt' % (origin_dir,trackdirid[i])  # 原始文件完整目录
        new_file_name = r'%s/%s-%s.txt' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        shutil.copyfile(origin_path, new_file_name)#复制文件

        n+=1
logging.info('the last group convert %d testing calib' % count)


######fix the calibfile
calibpath = os.path.join(path,'object_tracking/training/calib')  # 文件夹目录
files = os.listdir(calibpath)  # 得到文件夹下的所有文件名称
print('traingingcalib number is %d'%len(files))

for file in files:  # 遍历文件夹

    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开

        f = open(calibpath + "/" + file);  # 打开文件

        iter_f = iter(f);  # 创建迭代器

        aa = f.readlines()
        f.close()
        for i,data in enumerate(aa):
            if i==4:
                aa[4]=data.replace('R_rect','R0_rect:')
            if i==5:
                aa[5]=data.replace('Tr_velo_cam','Tr_velo_to_cam:')
            if i==6:
                aa[6]=data.replace('Tr_imu_velo','Tr_imu_to_velo:')

        with open(calibpath + "/" + file,'w') as fout:
            for data in aa:
                fout.write(data)

        fout.close()

calibpath = os.path.join(path,'object_tracking/testing/calib')  # 文件夹目录
files = os.listdir(calibpath)  # 得到文件夹下的所有文件名称
print('testingcalib number is %d'%len(files))

for file in files:  # 遍历文件夹

    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开

        f = open(calibpath + "/" + file);  # 打开文件

        iter_f = iter(f);  # 创建迭代器

        aa = f.readlines()
        f.close()
        for i,data in enumerate(aa):
            if i==4:
                aa[4]=data.replace('R_rect','R0_rect:')
            if i==5:
                aa[5]=data.replace('Tr_velo_cam','Tr_velo_to_cam:')
            if i==6:
                aa[6]=data.replace('Tr_imu_velo','Tr_imu_to_velo:')

        with open(calibpath + "/" + file,'w') as fout:
            for data in aa:
                fout.write(data)

        fout.close()


####### move training label_02
#fo = open('./trainval.txt', 'a')
outpath = os.path.join(path,'object_tracking/training/label_2')
for i in range(21):
    detections_by_frame = defaultdict(list)
    origin_dir = os.path.join(path, 'object/training/label_02')
    # origin_dir=path+'object/training/velodyne/%s/%s' % trackdirid[i],"{:06d}".format(n)
    origin_path = r'%s/%s.txt' % (origin_dir, trackdirid[i])  # 原始文件完整目录
    aa=[]
    with open(origin_path) as f:
        aa=f.readlines()
        for aa in aa:
            dd=aa.split(' ')
            if int(dd[3])==1:
                dd[3]=str(float(int(dd[3])/2))
            elif int(dd[3])==2:
                dd[3]=str(float(int(dd[3])/2))
#20.6.19在最后两列加入了帧号，trackid
            detections_by_frame[int(dd[0])].append('%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s'%(dd[2],dd[3],dd[4],dd[5],dd[6],dd[7],dd[8],dd[9],dd[10],dd[11],dd[12],dd[13],dd[14],dd[15],dd[16],dd[0],dd[1]))
        '''
        f_csv = csv.reader(f, delimiter=' ')
        for row in f_csv:
            frame_id = int(row[0])

            label = row[2]
            z0=row[3]
            z1=row[4]
            #z0,z1=map(int,row[3:4])
            alpha,x1, y1, x2, y2,height, width, length,x,y,z, rotation_y,score = map(float, row[5:17])
            detections_by_frame[frame_id].append({
                'label': label,
                'z0':z0,
                'z1':z1,
                'alpha':alpha,
                'left': x1,
                'top': y1,
                'right': x2,
                'bottom': y2,
                'height':height,
                'width':width,
                'length':length,
                'x':x,
                'y':y,
                'z':z,
                'rotation_y':rotation_y,
                'score':score
            })
        '''
    count = 0
    n = 000000
    #print(path + 'object/training/image_02/%s' % trackdirid[i])
    for root, dirs, files in os.walk(path + '/object/training/image_02/%s' % trackdirid[i]):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    #print(count)
    while n < count:
        new_file_name = r'%s/%s-%s.txt' % (outpath,trackdirid[i],"{:06d}".format(n))  # 文件新名字
        fo = open(new_file_name, 'a')
        frame_dets = detections_by_frame[n]
        for det in frame_dets:
            fo.write(det)
        #shutil.copyfile(origin_path, new_file_name)

        #fo.write('%s-%s\n' % (trackdirid[i],"{:06d}".format(n)))
        #     fo.write('%6d\n'%n)
        #     #n+=random.randint(1, 6)  # 依次读取每行
        n+= 1
logging.info('the last group convert %d training label' % count)


####2020.5.5加入对修改后的label文件做处理的过程：补充无标签的帧用dontcare，且将dontcare都放到最后行，根据deetection格式

labelpath = os.path.join(path,'object_tracking/training/label_2')  # 文件夹目录
files = os.listdir(labelpath)  # 得到文件夹下的所有文件名称
s = []
for file in files:  # 遍历文件夹

    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开

        f = open(labelpath + "/" + file);  # 打开文件

        iter_f = iter(f);  # 创建迭代器
        # name=file.split('-')
        # if len(f.readlines()) >0:
        #      pass
        # else:
        #      #f = open(path + "/" + file,'a')
        #      print(file)
        #      #f.write('DontCare -1 -1 -10.000000 1217.700000 137.630000 1242.000000 225.790000 -1000.000000 -1000.000000 -1000.000000 -10.000000 -1.000000 -1.000000 -1.000000')
        #      #f.write('DontCare -1 -1 -10.000000 1179.900000 181.690000 1212.900000 200.130000 -1000.000000 -1000.000000 -1000.000000 -10.000000 -1.000000 -1.000000 -1.000000')
        name = file.split('-')
        ###读取移动dontcare
        normal = []
        dontcare = []

        for line in iter_f:  # 遍历文件，一行行遍历，读取文本
            juge = line.split(' ')
            if juge[0] == 'DontCare':
                dontcare.append(line)
            else:
                normal.append(line)

        f = open(labelpath + "/" + file, 'w');

        f.writelines(normal)  # 直接将list写入txt文件里
        f.writelines(dontcare)
        f.close()
        
        #解决空文件
        f = open(labelpath + "/" + file);  # 打开文件
        if len(f.readlines()) >0:
            pass
        else:
            f = open(labelpath + "/" + file,'a')

            f.write('DontCare -1 -1 -10.000000 1217.700000 137.630000 1242.000000 225.790000 -1000.000000 -1000.000000 -1000.000000 -10.000000 -1.000000 -1.000000 -1.000000')
            logging.info('write dontcare in  file %s ' % file)
            f.close()

    # s.append(str) #每个文件的文本存到list中


#print(s) #打印结果
print('dataset convert done! Thank you!') #打印结果

