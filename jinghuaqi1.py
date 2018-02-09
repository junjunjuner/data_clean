import pandas as pd
import numpy as np
import re


#净水器CCM处理
df=pd.read_excel("jinghuaqi1.xlsx")
pd.set_option('display.max_rows',None)
solid_ccm_list=[]
for i in range(len(df.solid_ccm)):
    solid_ccm_list.append(df.solid_ccm[i])
    try:
        if (float(solid_ccm_list[i])>=3000 and float(solid_ccm_list[i])<5000):
            solid_ccm_list[i]='P1'
        elif (float(solid_ccm_list[i]) >= 5000 and float(solid_ccm_list[i]) < 8000):
            solid_ccm_list[i] = 'P2'
        elif (float(solid_ccm_list[i]) >= 8000 and float(solid_ccm_list[i]) < 12000):
            solid_ccm_list[i] = 'P3'
        elif (float(solid_ccm_list[i]) >=12000):
            solid_ccm_list[i] = 'P4'

    except:
        solid_ccm_list[i]=solid_ccm_list[i]
df.solid_ccm=solid_ccm_list

gas_ccm_list=[]
for i in range(len(df.gas_ccm)):
    gas_ccm_list.append(df.gas_ccm[i])
    gas_ccm_list[i]=str(gas_ccm_list[i]).replace('大于','')
    try:
        if (float(gas_ccm_list[i])>=300 and float(gas_ccm_list[i])<600):
            gas_ccm_list[i]='F1'
        elif (float(gas_ccm_list[i]) >= 600 and float(gas_ccm_list[i]) < 1000):
            gas_ccm_list[i] = 'F2'
        elif (float(gas_ccm_list[i]) >= 1000 and float(gas_ccm_list[i]) < 1500):
            gas_ccm_list[i] = 'F3'
        elif (float(gas_ccm_list[i]) >=1500):
            gas_ccm_list[i] = 'F4'

    except:
        gas_ccm_list[i]=gas_ccm_list[i]
df.gas_ccm=gas_ccm_list
df.to_excel("jinghuaqi1.xlsx",columns=df.columns,index=None)