# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 22:59
# @Author  : Zudy
# @FileName: c6.py


'''
1.处理时序数据变成稳定数据
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

inputfile = 'test1_four.xlsx'
data = pd.read_excel(inputfile ,sheet_name= 'Sheet2', index_col = '日期')
data1 = data['SS73210']

plt.rcParams['font.sans-serif']=['SimHei'] # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   # 用来正常显示负号

def draw_trend(timeseries, size):
    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    rol_mean = timeseries.rolling(window=size).mean()    # 对size个数据移动平均的方差
    # rol_std = timeseries.rolling(window=size).std()

    ax.plot(timeseries, color='blue', label='Original')
    ax.plot(rol_mean,color='red', label='Rolling Mean')

    # rol_std.plot(color='black', label='Rolling standard deviation')

    plt.legend(loc='best')
    ax.set_xticks('Rolling Mean & Standard Deviation')
    ax.set_xticks(['2018/09/01', '2018/10/01', '2018/11/01',
                   '2018/12/01', '2019/01/01', '2019/02/04', '2019/03/12'])

    plt.show()

draw_trend(data1, 18)


def draw_moving(timeSeries, size):
    # 绘图
    fig = plt.figure(facecolor='white')    # 对size个数据进行移动平均
    ax = fig.add_subplot(1, 1, 1)


    rol_mean = timeSeries.rolling(window=size).mean()    # 对size个数据进行加权移动平均
    rol_weighted_mean=timeSeries.ewm(halflife=size, min_periods=0, adjust=True, ignore_na=False).mean()

    ax.plot(timeSeries, color='blue', label='Original')
    ax.plot(rol_mean, color='red', label='Rolling Mean')
    ax.plot(rol_weighted_mean, color='black', label='Weighted Rolling Mean')

    ax.set_xticks('Rolling Mean & Standard Deviation')
    ax.set_xticks(['2018/09/01', '2018/10/01', '2018/11/01',
                   '2018/12/01', '2019/01/01', '2019/02/04', '2019/03/12'])
    plt.legend(loc='upper right')
    plt.show()

draw_moving(data1, 12)
