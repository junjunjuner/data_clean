import pandas as pd
import re
df=pd.read_excel("reshuihu1.xlsx",sheetname='Sheet2')
name=df.p_Name.values
# print(name)
c_list=[]
for n in name:
    capacity=re.findall('[0-9]*\.?[0-9]+L',str(n))
    print(capacity)
    if capacity:
        c_list.append(capacity[-1])
    else:
        c_list.append('')
df.capacity=c_list
df.to_excel("reshuihu2.xlsx",columns=df.columns,index=None)
# df.to_csv("jdjinghuaqi1.csv",columns=df.columns,index=None)