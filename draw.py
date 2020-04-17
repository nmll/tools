import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import linecache  #都指定行
# 从pyplot导入MultipleLocator类,这个类用于设置刻度间隔
valuedir='D:\cs_car.txt'
MOTA=[]
MOTP=[]
FN=[]
FP=[2723,1002,607,536,446,425,345,319,319,315,310,294,279,259,255,249,247,245,232,226,216,202,187,166,138,134,123,106,100,72,69,62,56,28,23,14,13,6]
precision=[0.7813,0.9051,0.9386,0.9439,0.9517,0.9525,0.9599,0.9604,0.9604,0.9597,0.9595,0.9596,0.9603,0.9615,0.9505,0.9602,0.9585,0.9583,0.9574,0.9561,0.9556,0.9562,0.9568,0.9589,0.9632,0.9599,0.9608,0.9640,0.9613,0.9702,0.9678,0.9659,0.9652,0.9779,0.9788,0.9828,0.9724,0.9853]
x_values =[]
y_values=[]


id=151

for i in range(38):
    value=[]
    value=linecache.getline('D:\cs_car.txt',id)
    #print(value,id)
    value=value.split(' ')
    print(value)
    MOTA.append(float(value[1]))
    MOTP.append(float(value[2]))
    FN.append(int(value[-1]))
    #FP.append(value[-4])
    #precision.append(value[15])
    id-=4
# [0.0449,0.0501,0.0905,0.1165,0.1337,0.1636,0.1832, 0.2184,0.2462,0.2566,0.2971,0.3126,0.3230,0.3345,
# 0.3574,0.3838,0.4113,0.4374,0.4619,0.4874, 0.5203,0.5289,0.5655,0.5863,0.6116,0.6403,0.6563,0.6918,0.7064,0.7336,
# 0.7336,0.7743,0.7879,0.8051,0.8186,0.8335,0.7958,0.6022]
x_values=precision
y_values=FP

plt.plot(x_values, y_values, c='green')

# for a, b in zip(x_values, y_values):
#     plt.text(a,b,(a,b),ha='center', va='bottom', fontsize=10)   #在每个点显示值
#plt.title('AP curve', fontsize=10)#顶上方显示字符串

plt.tick_params(axis='both', which='major', labelsize=10)

plt.xlabel('precision', fontsize=10)

plt.ylabel('FP', fontsize=10)

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

plt.xlim(0.6, 1.0)

# 把x轴的刻度范围设置为-0.5到11,因为0.5不满一个刻度间隔,所以数字不会显示出来,但是能看到一点空白

plt.ylim(0,3000)

# 把y轴的刻度范围设置为-5到110,同理,-5不会标出来,但是能看到一点空白


plt.show()
