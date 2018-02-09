import pandas as pd
import numpy as np
import re


#品牌处理
df=pd.read_csv("jddfb_items (复件).csv")
pd.set_option('display.max_rows',None)
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    # if type(brand_list[i])==str:
    #     brand_list[i]=re.sub('\(.*?\)','',brand_list[i])
    if '松下' in  brand_list[i]:
        brand_list[i] = "松下"
    if '象印' in brand_list[i]:
        brand_list[i] = "象印"
    if '苏泊尔' in brand_list[i]:
        brand_list[i] = "苏泊尔"
    if '凯伍德' in brand_list[i]:
        brand_list[i] = "凯伍德"
    if '飞利浦' in brand_list[i]:
        brand_list[i] = "飞利浦"
    if '日立' in brand_list[i]:
        brand_list[i] = "日立"
    if '松心' in brand_list[i]:
        brand_list[i] = "松心"
    if '夏普' in brand_list[i]:
        brand_list[i] = "夏普"
    if '美的' in brand_list[i]:
        brand_list[i] = "美的"
    if brand_list[i] == "SONGX":
        brand_list[i] = "松心"
    if '东芝' in brand_list[i]:
        brand_list[i] = "东芝"
    if brand_list[i] == "PHILIPS":
        brand_list[i] = "飞利浦"
    if brand_list[i] == "KUFU":
        brand_list[i] = "酷福"
    if brand_list[i] == "THERMOS":
        brand_list[i] = "膳魔师"
    if 'CUCHEN' in brand_list[i]:
        brand_list[i] = "酷晨"
    if 'CUCKOO' in brand_list[i]:
        brand_list[i] = "福库"
    if '虎牌' in brand_list[i]:
        brand_list[i] = "虎牌"
    if 'BALMUDA' in brand_list[i]:
        brand_list[i] = "巴慕达"
    if 'Tefal' in brand_list[i]:
        brand_list[i] = "特福"
    if '小米' in brand_list[i]:
        brand_list[i] = "小米"
    if '三菱' in brand_list[i]:
        brand_list[i] = "三菱"
    if 'Sanki' in brand_list[i]:
        brand_list[i] = "山崎"
    if brand_list[i] == "CLARA":
        brand_list[i] = "克拉拉"
    if brand_list[i] == "sansui":
        brand_list[i] = "山水"
    if brand_list[i] == "HONG":
        brand_list[i] = "红牌"
    if brand_list[i] == "WHITE TIGER":
        brand_list[i] = "威泰戈"
    if brand_list[i] == "WHITE TIGER":
        brand_list[i] = "威泰戈"
    if brand_list[i] == "WHITE TIGER":
        brand_list[i] = "威泰戈"
# print(brand_list)
df.brand=brand_list
df.to_excel("jddfb.xlsx",columns=df.columns,index=None)