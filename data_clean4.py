import pandas as pd
'''''''''''
将三个网站的数据合并在一个表中
'''''''''''

df1=pd.read_csv("jd_rsh.csv",encoding='utf8')
df2=pd.read_csv("gm_rsh.csv",encoding='utf8')
# df=pd.read_excel("jmjinghuaqi-格力大松合并.xlsx",encoding='utf8')
df3=pd.read_csv("sn_rsh.csv",encoding='utf8')
df1=df1.append(df3)
df1=df1.append(df2)
df1.to_excel("reshuihu.xlsx",index=None)



