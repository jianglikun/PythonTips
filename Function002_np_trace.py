from numpy import np

#np.trace 用于计算对角线的和

np.trace(np.eye(3))
#3.0

a = np.arange(8).reshape((2,2,2))
np.trace(a)
#array([6, 8])

#来个比较个性的

import numpy as np

s1='agtcgtaatgc'

s2="cgaa"

a = np.fromstring(s1,'S1')==np.fromstring(s2,'S1').reshape(-1,1)
#比较两个字符串，得到一个True Flase矩阵，矩阵大小是len(s2)=4  X len(s1)=11

i = max(range(len(s1)), key= a.trace)
#max内部的参数key，是针对循环里变量加上一个参数，a.trace(0:11)的意思是，trace只计算方形的矩阵，a是4*11，所以顺次计算11个矩阵的对角线之和，max取最大
