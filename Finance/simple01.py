import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
data = pd.read_csv('D:\whatsoever\Finance\TSLA.csv',header=None,sep=' ') 
day_num = data.shape[0] - 1
ops = np.zeros((day_num))
eds = np.zeros((day_num))
his = np.zeros((day_num))
los = np.zeros((day_num))

plot_x = np.zeros((day_num))

for i in range(0,day_num):
    day_data = data[0][i+1]
    st = day_data.split(',')
    ops[i] = st[1]
    his[i] = st[2]
    los[i] = st[3]
    eds[i] = st[4]
    plot_x[i] = i + 1
    
ops_diff = np.zeros((day_num))
eds_diff = np.zeros((day_num))
for i in range(1,day_num-1):
    ops_diff[i] = (ops[i+1] - ops[i-1]) * 0.5
    eds_diff[i] = (eds[i+1] - eds[i-1]) * 0.5
    
opseds_diff = ops_diff - eds_diff
    
ops_diff4 = np.zeros((day_num))
eds_diff4 = np.zeros((day_num))
for i in range(2,day_num-2):
    ops_diff4[i] = (-ops[i-2]+8*ops[i-1]-8*ops[i+1]+ops[i+2])/12
    eds_diff4[i] = (-eds[i-2]+8*eds[i-1]-8*eds[i+1]+eds[i+2])/12
    
opseds_diff4 = ops_diff4 - eds_diff4

def cm_to_inch(value):
    return value/2.54
    
plt.figure(figsize=(cm_to_inch(25), cm_to_inch(15)))
plt.xlabel("everday open ")#x轴上的名字
plt.plot(plot_x,ops)
plt.show()
plt.xlabel("everday close ")#x轴上的名字
plt.plot(plot_x,eds)
plt.show()
plt.xlabel("everday open 1st derivate")#x轴上的名字
plt.plot(plot_x,ops_diff)
plt.show()
plt.xlabel("everday close 1st derivate")#x轴上的名字
plt.plot(plot_x,eds_diff)
plt.show()
plt.xlabel("everday open 4st derivate")#x轴上的名字
plt.plot(plot_x,ops_diff4)
plt.show()
plt.xlabel("everday close 4st derivate")#x轴上的名字
plt.plot(plot_x,eds_diff4)
plt.show()
plt.xlabel("everday open close 1st diff")#x轴上的名字
plt.plot(plot_x,opseds_diff)
plt.show()
plt.xlabel("everday open close 4st diff")#x轴上的名字
plt.plot(plot_x,opseds_diff4)
plt.show()
plt.xlabel("everday open ")#x轴上的名字
plt.plot(plot_x,ops)
plt.show()
plt.xlabel("everday close ")#x轴上的名字
plt.plot(plot_x,eds)
plt.show()