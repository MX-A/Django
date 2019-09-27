import numpy as np
import matplotlib.pyplot as plt
import random,time
from mytest.myapp.read_data import read_data
# stnum ="250"
# print(int(stnum))
while True:
    time.sleep(1)
    cache_data=open('mytest/myapp/cache.txt','w')
    UA = random.uniform(10, 10.3)
    UB = random.uniform(10, 10.3)
    UC = random.uniform(10, 10.3)
    IA = random.uniform(10, 10.3)
    IB = random.uniform(10, 10.3)
    IC = random.uniform(10, 10.3)
    cache_data.write('NEW\n')
    cache_data.write('SZU'+str(UA)+'A\n')
    cache_data.write('SZU'+str(UB)+'B\n')
    cache_data.write('SZU'+str(UC)+'C\n')
    cache_data.write('SZU'+str(IA)+'D\n')
    cache_data.write('SZU'+str(IB)+'E\n')
    cache_data.write('SZU'+str(IC)+'F\n')
    cache_data.close()
    # UA, UB, UC, IA, IB, IC=read_data()
#    print(UA, UB, UC, IA, IB, IC)
# cache_data=open('cache.txt','r+')
# datalines=cache_data.readlines()
# if datalines[0] == 'NEW\n':
#     for dataline in datalines:
#         num=len(dataline)
#         if dataline[num-2] == 'A':
#             UA=float(dataline[3:num-2])
#             print(UA)
#         elif dataline[num-2] == 'B':
#             UA=float(dataline[3:num-2])
#             print(UA)
#         elif dataline[num - 2] == 'C':
#             UA = float(dataline[3:num - 2])
#             print(UA)
#         elif dataline[num - 2] == 'D':
#             UA = float(dataline[3:num - 2])
#             print(UA)
#         elif dataline[num - 2] == 'E':
#             UA = float(dataline[3:num - 2])
#             print(UA)
#         elif dataline[num - 2] == 'F':
#             UA = float(dataline[3:num - 2])
#             print(UA)
# else:
#     print("没有新数据")
# cache_data.seek(0)
# cache_data.truncate()
# cache_data.close()
# s = []
# X=np.arange(0,100)
# for i in range(0,100):
#     num=random.randint(10,100)
#     s.append(num)
#     print(s)
# plt.plot(X,s)
# plotpath = r'H:\django-test\mytest\static\fig.png'
# plt.savefig(plotpath)

