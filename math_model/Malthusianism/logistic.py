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
Nt = 5.5 # 初始状态人口数
N0=Nt
tx=[]
Nty=[]
K = 20
r = 1.9
for i in range(0,50):
    t+=1
    tx.append(t)
    Nt=(1+r)*Nt-(r/K)*(pow(Nt,2))
    Nty.append(Nt)

plt.plot(tx,Nty,color="red")
plt.title("based with r="+str(r)+" and K="+str(K)+" and N0="+str(N0))
plt.xlabel("t",color="blue")
plt.ylabel("Nt",color="blue")
plt.show()





