import numpy as np
import matplotlib.pyplot as plt

'''
Nt+1 = (1+r)Nt - (r/K)*(Nt^2)
Nt:                t年的人口数
r:                 人口自然增长率（常量）
K:                 最多人口数（常量）
真实自然增长率:     r*(1-N/K)      
'''

t=0
Nt = 0 # 初始状态人口数
N0=Nt
Nt_1=[]
Nt_0=[N0]
K = 20
r = 1.9
cnt = 0
for i in range(0,10000):
    Nt_0.append(Nt)
    Nt += 0.005
    Nt1=(1+r)*Nt-(r/K)*(pow(Nt,2))
    t+=0.1
    if(Nt1>0):
        Nt_1.append(Nt1)
        cnt=i
    if(Nt1<0):
        cnt=i
        break


Nt_1 = Nt_1[:cnt]
Nt_0 = Nt_0[:cnt]
# plt.plot(Nt,Nt_0,color="red")
plt.plot(Nt_0,Nt_1,color='green')
plt.scatter(20,20,c='red') # plt.scatter(x, y, s=20, c='b') s是大小，标出K点所在位置
plt.title("based with r="+str(r)+" and K="+str(K)+" and N0="+str(N0))
plt.xlabel("Nt",color="blue")
plt.ylabel("Nt+1",color="blue")
plt.show()





