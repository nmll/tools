import numpy as np



u= np.zeros((5,2))
a = np.random.randn(5,1)#产生高斯随机变量
u=u+2  #2自动扩展
x=np.log(u).T

print(np.sum(u))#求矩阵元素的所有项的和
assert (a.shape==(5,1)) #断言错误不会继续执行
print(x.sum(axis=0))#按行或列来求和
print (np.dot(u,x))#矩阵相乘
