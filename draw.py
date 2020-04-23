# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import linecache  #指定某行
# 从pyplot导入MultipleLocator类,这个类用于设置刻度间隔
sa_valuedir=r'D:\code\project\results\tracking_result\car_SASSD_det_val\summary_car_average_eval3D.txt'
por_valuedir=r'D:\code\project\results\tracking_result\car_pointrcnn3d_det_val\summary_car_average_eval3D.txt'


####该数据为SA-SSD——AB3Dtracking数据
sa_score_thr=[]
por_score_thr=[]
MOTA_sa=[]
MOTA_por=[]
MOTP=[]
sa_FN=[]
por_FN=[]
FP=[2723,1002,607,536,446,425,345,319,319,315,310,294,279,259,255,249,247,245,232,226,216,202,187,166,138,134,123,106,100,72,69,62,56,28,23,14,13,6]
precision=[0.7813,0.9051,0.9386,0.9439,0.9517,0.9525,0.9599,0.9604,0.9604,0.9597,0.9595,0.9596,0.9603,0.9615,0.9505,0.9602,0.9585,0.9583,0.9574,0.9561,0.9556,0.9562,0.9568,0.9589,0.9632,0.9599,0.9608,0.9640,0.9613,0.9702,0.9678,0.9659,0.9652,0.9779,0.9788,0.9828,0.9724,0.9853]


####下面是测试SA-SSDdetection的FN值
sa_easy_detection_FN=['6515.0000', '6353.0000', '6190.0000', '6027.0000', '5864.0000', '5702.0000', '5539.0000', '5376.0000', '5213.0000', '5050.0000', '4887.0000', '4723.0000', '4560.0000', '4397.0000', '4234.0000', '4069.0000', '3907.0000', '3743.0000', '3579.0000', '3416.0000', '3252.0000', '3088.0000', '2924.0000', '2760.0000', '2596.0000', '2432.0000', '2268.0000', '2102.0000', '1936.0000', '1770.0000', '1603.0000', '1438.0000', '1275.0000', '1111.0000', '947.0000', '780.0000', '616.0000', '449.0000', '279.0000', '98.0000', '6.0000']
#相应的阈值
easy_detection_thr=[0.91632229,0.8766188,0.86872506,0.86281592,0.85781515,0.85430998,
               0.85013556,0.84674227,0.84264988,0.8395766,0.83652854,0.83343053,
 0.83022612,0.82642281,0.82328266,0.82052767,0.81789982,0.81474161,
               0.81157494,0.80826551,0.80540872,0.8015334,0.79829657,0.79449582,
 0.79070264,0.786973,0.782875,0.7778042,0.77269882,0.76768947,
               0.76211435,0.75570363,0.74880242,0.74267411,0.73483646,0.72417015,
 0.71144164,0.69685191,0.66772562,0.60030782,0.30716959]

sa_mid_detection_FN=['16060.0000', '15659.0000', '15258.0000', '14856.0000', '14455.0000', '14053.0000', '13652.0000', '13250.0000', '12849.0000', '12447.0000', '12046.0000', '11644.0000', '11243.0000', '10841.0000', '10440.0000', '10038.0000', '9637.0000', '9235.0000', '8834.0000', '8432.0000', '8030.0000', '7629.0000', '7227.0000', '6825.0000', '6422.0000', '6021.0000', '5617.0000', '5216.0000', '4813.0000', '4411.0000', '4003.0000', '3594.0000', '3185.0000', '2781.0000', '2369.0000', '1959.0000', '1542.0000', '1115.0000', '677.0000', '503.0000']
mid_detection_thr=[0.91730756,0.86782366,0.85707486, 0.84955519, 0.84231126, 0.83610189,
 0.83027416, 0.82418978, 0.81939965, 0.81399632, 0.80908477, 0.80364597,
 0.79869646, 0.79324996, 0.78848118, 0.78300983, 0.77763313, 0.77154112,
 0.76534909, 0.75783342, 0.75117391, 0.74384594, 0.73613685, 0.72694474,
 0.71901506, 0.70979029, 0.70092565, 0.69054627, 0.67785043, 0.66458136,
 0.64929229, 0.63174695, 0.61356395, 0.59431273, 0.57007641, 0.5430584,
 0.5036056,  0.44608203, 0.35913181, 0.30125526]

sa_diff_detection_FN=['21326.0000', '20794.0000', '20261.0000', '19727.0000', '19194.0000', '18661.0000', '18128.0000', '17595.0000', '17062.0000', '16528.0000', '15995.0000', '15462.0000', '14929.0000', '14396.0000', '13863.0000', '13329.0000', '12796.0000', '12263.0000', '11730.0000', '11196.0000', '10661.0000', '10128.0000', '9593.0000', '9060.0000', '8526.0000', '7990.0000', '7449.0000', '6910.0000', '6374.0000', '5838.0000', '5299.0000', '4759.0000', '4219.0000', '3679.0000', '3134.0000', '2587.0000', '2029.0000', '1474.0000', '1089.0000']
diff_detection_thr=[0.91737008, 0.86408645, 0.85211277, 0.84249592, 0.83468622, 0.82650942,
 0.81965423, 0.81283402, 0.80651343, 0.79995954, 0.79343259, 0.78708535,
 0.78034359, 0.77372462, 0.765957 ,  0.75782162, 0.75000775, 0.74194783,
 0.73280936, 0.72344911, 0.71403778, 0.70465904, 0.69483304, 0.68321246,
 0.67067331, 0.65717316, 0.64243031, 0.62775773, 0.61717314, 0.60524482,
 0.58999211, 0.5702886,  0.55099469, 0.52749765, 0.49749663, 0.46361551,
 0.42155367, 0.36139616, 0.3004151 ]


sa_easy_detection_FN=[float(i) for i in sa_easy_detection_FN]
sa_mid_detection_FN=[float(i) for i in sa_mid_detection_FN]
sa_diff_detection_FN=[float(i) for i in sa_diff_detection_FN]


###########

x_values =[]
y_values=[]


sa_valueid=143
por_valueid=151

for i in range(30):
    ####读sa-ssd+AB3d的3d评价工具结果
    sa_value=[]
    sa_con=[]
    sa_value=linecache.getline(sa_valuedir,sa_valueid)
    #print(value,id)
    value=sa_value.split(' ')
    print(value)
    MOTA_sa.append(float(value[1]))
    #MOTP.append(float(value[2]))
    sa_FN.append(int(value[-1]))
    sa_con=linecache.getline(sa_valuedir,sa_valueid-2)
    confidence=sa_con.split(' ')
    sa_score_thr.append(float(confidence[4].replace(',','')))
    #FP.append(value[-4])
    #precision.append(value[15])
    sa_valueid-=4

for i in range(38):
    ####读poiontrcnn结果
    por_value = []
    por_con = []
    por_value = linecache.getline(por_valuedir, por_valueid)
    # print(value,id)
    value = por_value.split(' ')
    print(value)
    MOTA_por.append(float(value[1]))
    # MOTP.append(float(value[2]))
    por_FN.append(int(value[-1]))
    por_con = linecache.getline(por_valuedir, por_valueid-2)
    confidence = por_con.split(' ')
    por_score_thr.append(float(confidence[4].replace(',','')))
    # FP.append(value[-4])
    # precision.append(value[15])

    por_valueid-=4
for i in range(len(por_score_thr)):#缩放pointrcnn的横坐标到0-1
    por_score_thr[i]=(por_score_thr[i]+1)/12.0



############下面绘图过程

x_values=easy_detection_thr
y_values=sa_easy_detection_FN


plt.plot(sa_score_thr, sa_FN, color='red', label='SASSD+AB3d-FN') #画另一条对比的曲线
plt.plot(x_values, y_values, c='green',label='SASSD-easy-FN')
#plt.plot(por_score_thr, MOTA_por, color='red', label='pointrcnn-MOTA') #画另一条对比的曲线
plt.plot(mid_detection_thr, sa_mid_detection_FN, color='blue', label='SASSD-mid-FN') #画另一条对比的曲线
plt.plot(diff_detection_thr, sa_diff_detection_FN, color='yellow', label='SASSD-diff-FN') #画另一条对比的曲线


# for a, b in zip(x_values, y_values):
#     plt.text(a,b,(a,b),ha='center', va='bottom', fontsize=10)   #在每个点显示值

#plt.title('AP curve', fontsize=10)#顶上方显示字符串

plt.tick_params(axis='both', which='major', labelsize=10)

plt.xlabel('score_thr', fontsize=10)

plt.ylabel('FN', fontsize=10)

x_major_locator = MultipleLocator(0.1)

# 把x轴的刻度间隔设置为1,并存在变量里

y_major_locator = MultipleLocator(1000)

# 把y轴的刻度间隔设置为10,并存在变量里

ax = plt.gca()

# ax为两条坐标轴的实例

ax.xaxis.set_major_locator(x_major_locator)

# 把x轴的主刻度设置为1的倍数

ax.yaxis.set_major_locator(y_major_locator)

# 把y轴的主刻度设置为10的倍数

plt.xlim(0, 1.0)

# 把x轴的刻度范围设置为-0.5到11,因为0.5不满一个刻度间隔,所以数字不会显示出来,但是能看到一点空白

plt.ylim(0,7000)

# 把y轴的刻度范围设置为-5到110,同理,-5不会标出来,但是能看到一点空白

plt.legend() # 显示图例
plt.show()
