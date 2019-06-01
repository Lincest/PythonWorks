
import numpy as np
import pandas as pd
from pandas import DataFrame
pd.set_option('max_columns', 10)
pd.set_option('max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.2f' % x) # 禁用科学计数法

a = pd.read_excel("元器件清单.xlsx")#,index_col='index') #header=1, nrows=17, usecols=3)
print(a)
b = DataFrame(a)
print(b.iat[1,1])
j=1
for i in range(0, b.shape[0]):
    print(b.iat[i,1])
    print(b.iat[i, 2])
    print(b.iat[i, 3])
    print(b.iat[i, 4])
    j+=1
# print(DataFrame(a).shape[0])行数
# for i in range(0,DataFrame(a).shape[0]):
#     print(i)
# a.head(0)