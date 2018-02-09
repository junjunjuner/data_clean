import pandas as pd
import numpy as np
import re


#品牌处理
df=pd.read_excel("reshuihu.xlsx")
pd.set_option('display.max_rows',None)
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    brand_list[i]=str(brand_list[i]).split(" ")[0]
# print(brand_list)
df.brand=brand_list
df.to_excel("reshuihu1.xlsx",columns=df.columns,index=None)
