import pandas as pd
import numpy as np
import re

'''''''''''
品牌处理(总)
'''''''''''
df=pd.read_csv("jdjinghuaqi.csv")
pd.set_option('display.max_rows',None)
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(str(df.brand[i]).lower())
    # if type(brand_list[i])==str:
    #     brand_list[i]=re.sub('\(.*?\)','',brand_list[i]
    if "碧然德" in brand_list[i] or "BRITA" in brand_list[i] or "Brita" in brand_list[i] or "brita" in brand_list[i]:
        brand_list[i] = "碧然德"
    if "松下" in brand_list[i]:
        brand_list[i] = "松下"
    if "可滋瀑瑞" in brand_list[i] or "Purifree" in brand_list[i] or "purifree" in brand_list[i]:
        brand_list[i] = "可滋瀑瑞"
    if "倍世" in brand_list[i] or "BWT" in brand_list[i] or "bwt" in brand_list[i]:
        brand_list[i] = "倍世"
    if "波尔德" in brand_list[i] or "PearlCo" in brand_list[i] or "pearlCo" in brand_list[i]:
        brand_list[i] = "波尔德"
    if "宝洁" in brand_list[i] or "PUR" in brand_list[i] or "Pur" in brand_list[i] or "pur" in brand_list[i]:
        brand_list[i] = "宝洁"
    if "伊莱克斯" in brand_list[i] :
        brand_list[i] = "伊莱克斯"
    if "夏普" in  brand_list[i] or "sharp" in  brand_list[i] or "SHARP" in  brand_list[i]:
        brand_list[i] = "夏普"
    if "飞利浦" in brand_list[i] or "Philips" in brand_list[i] or "PHILIPS" in brand_list[i]:
        brand_list[i] = "飞利浦"
    if "Waterchef" in brand_list[i] or "水厨神" in brand_list[i] or "waterchef" in brand_list[i]:
        brand_list[i] = "水厨神"
    if "阿克萨纳" in brand_list[i] or "Aquasana" in brand_list[i] or "aquasana" in brand_list[i]:
        brand_list[i] = "阿克萨纳"
    if "莱卡" in brand_list[i] or "Laica" in brand_list[i] or "laica" in brand_list[i]:
        brand_list[i] = "莱卡"
    if "霍尼韦尔" in brand_list[i] or "Honeywell" in brand_list[i] or "honeywell" in brand_list[i]:
        brand_list[i] = "霍尼韦尔"
    if "大金" in brand_list[i] or "Daikin" in brand_list[i] or "daikin" in brand_list[i]:
        brand_list[i] = "大金"
    if "巴慕达" in brand_list[i] or "Balmuda" in brand_list[i] or "balmuda" in brand_list[i]:
        brand_list[i] = "巴慕达"
    if "布鲁雅尔" in brand_list[i] or "Blueair" in brand_list[i] or "blueair" in brand_list[i]:
        brand_list[i] = "布鲁雅尔"
    if "日立" in brand_list[i] or "Hitachi" in brand_list[i] or "hitachi" in brand_list[i]:
        brand_list[i] = "日立"
    if "戴森" in brand_list[i] or "Dyson" in brand_list[i] or "dyson" in brand_list[i]:
        brand_list[i] = "戴森"
    if "博雅" in brand_list[i] or "Beurer" in brand_list[i] or "beurer" in brand_list[i]:
        brand_list[i] = "博雅"
    if "爱客" in brand_list[i] or "Iqair" in brand_list[i] or "iqair" in brand_list[i]:
        brand_list[i] = "爱客"
    if "奥斯汀" in brand_list[i] or "austin" in brand_list[i] or "Austin" in brand_list[i]:
        brand_list[i] = "奥斯汀"
    if "小米" in brand_list[i] or "mi" in brand_list[i] or "Mi" in brand_list[i]:
        brand_list[i] = "小米"
    if "沃尔玛" in brand_list[i] or "walmart" in brand_list[i] or "Walmart" in brand_list[i]:
        brand_list[i] = "沃尔玛"
    if "文塔" in brand_list[i] or "venta" in brand_list[i] or "Venta" in brand_list[i]:
        brand_list[i] = "文塔"
    if "tcl" in brand_list[i] or "TCL" in brand_list[i]:
        brand_list[i] = "TCL"
    if "威发" in brand_list[i] or "vifa" in brand_list[i]:
        brand_list[i] = "威发"
    if "三星" in brand_list[i] or "samsung" in brand_list[i]:
        brand_list[i] = "三星"
    if "斯泰得乐" in brand_list[i] or "stadler form" in brand_list[i]:
        brand_list[i] = "斯泰得乐"
    if "博瑞客" in brand_list[i] or "boneco" in brand_list[i]:
        brand_list[i] = "博瑞客"
    if "麦克赛尔" in brand_list[i] or "maxell" in brand_list[i]:
        brand_list[i] = "麦克赛尔"
    if "匠品" in brand_list[i] or "sis" in brand_list[i]:
        brand_list[i] = "匠品"
    if "霍姆斯" in brand_list[i] or "holmes" in brand_list[i]:
        brand_list[i] = "霍姆斯"
    if "菲尔萃" in brand_list[i] or "filtrete" in brand_list[i]:
        brand_list[i] = "菲尔萃"
    if "艾弗瑞" in brand_list[i] or "airfree" in brand_list[i]:
        brand_list[i] = "艾弗瑞"
    if "爱娃狮" in brand_list[i] or "airvax" in brand_list[i]:
        brand_list[i] = "爱娃狮"
    if "得康氧" in brand_list[i] or "teqoya" in brand_list[i]:
        brand_list[i] = "得康氧"
    if "德龙" in brand_list[i] or "delonghi" in brand_list[i]:
        brand_list[i] = "德龙"
    if "达乐" in brand_list[i] or "dahle" in brand_list[i]:
        brand_list[i] = "达乐"
    if "lightair" in brand_list[i] :
        brand_list[i] = "lightair"
    if "欧西亚" in brand_list[i] or "oregon scientific" in brand_list[i]:
        brand_list[i] = "欧西亚"
    if "爱屋安" in brand_list[i] or "envion" in brand_list[i]:
        brand_list[i] = "爱屋安"
    if "范罗士" in brand_list[i] or "fellowes" in brand_list[i]:
        brand_list[i] = "范罗士"
    if "博世" in brand_list[i] or "bosch" in brand_list[i]:
        brand_list[i] = "博世"
    if "cado" in brand_list[i]:
        brand_list[i] = "CADO"
    if "lg" in brand_list[i]:
        brand_list[i] = "LG"
    # if brand_list[i] == "greenis":
    #     brand_list[i] = "格丽思"
    # if brand_list[i] == "Baumatic":
    #     brand_list[i] = "博曼帝克"
    # if brand_list[i] == "CASDON":
    #     brand_list[i] = "凯度"
    # if brand_list[i] == "COUSS":
    #     brand_list[i] = "卡士"
    # if brand_list[i] == "卡氏":
    #     brand_list[i] = "卡士"
    # if brand_list[i] == "daogrs":
    #     brand_list[i] = "迪奥格斯"
    # if brand_list[i] == "Depelec":
    #     brand_list[i] = "德普"
    # if brand_list[i] == "DEGURU":
    #     brand_list[i] = "地一"
    # if brand_list[i] == "NOSTALGIA ELECTRICS":
    #     brand_list[i] = "诺思得其"
    # if brand_list[i] == "sansui":
    #     brand_list[i] = "山水"
    # if brand_list[i] == "WHITE TIGER":
    #     brand_list[i] = "威泰戈"

# print(brand_list)
df.brand=brand_list
df.to_csv("jdjinghuaqi1.csv",columns=df.columns,index=None)

'''''''''''''''''
10+air 侍家
AAF 雅风
AAVI 雅威
ADAWO 爱达屋
air 艾尔康居
AIRBURG 空气堡
Allerair 欧乐
ALONDES 欧朗德斯
am:10 微森林
apet 爱派
askoree 韩乐
BD 博大
BlueHorizon 海润
Dephina 德菲兰
DESAY 德赛
Brit 波尔德
ECOBAO 生态宝
ENA 钮爱
Enchoy 恩科
EraClean 艾瑞克林
ermake ji 二马
FOGIBLOC 贝罗
FZM 方米
GPUSEN 吉浦森
HealthPro 爱客
hious 凯优
Hoover 胡佛
HYUNDAI 现代
IDEAL LUFT 安德露
Innerwell 易能韦尔
IRIS 爱丽思
KARCHER 凯驰
KING HONOR 霍尔
Lightair 莱特艾尔
LUFTRUM 瑞际
MEIMEI 美美
MR.FUTURE 未来先生
NTCOAT 纳琦环保
PHILIPS 飞利浦
REHAU 瑞好
RHEIN TEC 倍适
SAIFI 赛菲
Sansui 山水
SheerAIRE 席爱尔
Six star 六星
Skyish 施凯西
SOLEUSAIR 厨卫宝
TDB 深呼吸
Telamon 泰拉蒙
UCHEER 友好
V 维尔森
wentry 万全
WETZEL 魏茨
xdoni 喜多多
XN 艾灸
YHF 永华
'''''''''''''''''