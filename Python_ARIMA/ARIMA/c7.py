# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 23:49
# @Author  : Zudy
# @FileName: c7.py

'''
1.处理时序数据变成稳定数据
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

inputfile = 'D:/Python/Python_learning/HBUT/预处理/test1_four.xlsx'
data = pd.read_excel(inputfile ,sheet_name= 'Sheet4', index_col = '日期')


plt.rcParams['font.sans-serif']=['SimHei'] # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   # 用来正常显示负号


def decompose(timeseries):
    # 返回包含三个部分 trend（趋势部分） ， seasonal（季节性部分） 和residual (残留部分)
    decomposition = seasonal_decompose(timeseries)

    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    plt.subplot(411)
    plt.plot(timeseries, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    return trend, seasonal, residual

trend, seasonal, residual = decompose(data['SS73210'])
residual.dropna(inplace=True)
# draw_trend(residual, 12)
# teststationarity(residual)
