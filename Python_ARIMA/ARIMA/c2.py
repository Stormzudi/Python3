# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 22:50
# @Author  : Zudy
# @FileName: c2.py

'''
1.毕业论文（销量预测）
2.运用模型：ARIMA
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns     #seaborn画出的图更好看，且代码更简单，缺点是可塑性差
from statsmodels.graphics.tsaplots import plot_acf  #自相关图
from statsmodels.tsa.stattools import adfuller as ADF  #平稳性检测
from statsmodels.graphics.tsaplots import plot_pacf    #偏自相关图
from statsmodels.stats.diagnostic import acorr_ljungbox    #白噪声检验
from statsmodels.tsa.arima_model import ARIMA  #引入ARIMA模型
#seaborn 是建立在matplotlib之上的


#文件的导入，和data的选取。
inputfile = 'D:/Python/Python_learning/HBUT/model_3/test_four.xlsx'
data = pd.read_excel(inputfile ,sheet_name= 'Sheet2', index_col = '日期')
print(data.head())
print(data[-5:])
data_1 = data['SS81346']; data_2 = data['SS81004']
data_3 = data['SS73210']; data_4 = data['SS81516']; data_5 = data['SS81376']
data_ = data_1

#seaborn设置背景
sns.set(color_codes=True)
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.rcParams['figure.figsize'] = (8, 5)   #设置输出图片大小


#自相关图
#自相关图显示自相关系数长期大于零，说明时间序列有很强的相关性
f = plt.figure(facecolor='white')
ax1 = f.add_subplot(1, 1, 1)
data_drop = data_.dropna()  #将数据data dropna()
plot_acf(data_drop, lags=31, ax=ax1)


#平稳性检查
print(u'原始序列的ADF检验结果为：')
print(ADF(data_)) #通过导入的ADF模块返回销量的平稳性检查
#单位根统计量对应的p的值显著大于0.05，最终判断该序列是非平稳序列

#1阶差分后的时序图
f = plt.figure(facecolor='white')
ax2 = f.add_subplot(1, 1, 1)
D_data = data_.diff().dropna()   #1阶差分，丢弃na值
D_data.plot(ax = ax2)
print(u'一阶差分序列的ADF检验结果为：')
print(ADF(D_data))
#输出p值远小于0.05，所以1阶差分之后是平稳非白噪声序列


#绘制一阶差分前后的图像
f = plt.figure(facecolor='white')
ax3 = f.add_subplot(2, 1, 1)
plot_acf(D_data, lags=31, ax=ax3) #自相关
ax4 = f.add_subplot(2, 1, 2)
plot_pacf(D_data, lags=31, ax=ax4) #偏相关

'''
#相对最优模型（p,q）
data_ = data_.astype(float)  #销量转为float类型
#定阶
pmax = int(len(D_data)/30) #一般阶数不超过length/10
qmax = int(len(D_data)/30) #一般阶数不超过length/10
bic_matrix = [] #bic矩阵
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try: #存在部分报错，所以用try来跳过报错。
            tmp.append(ARIMA(data_, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix) #从中可以找出最小值
p, q = bic_matrix.stack().idxmin() #先用stack展平，然后用idxmin找出最小值位置。
print(u'BIC最小的p值和q值为：%s、%s' %(p, q))
'''

p = 6
q = 0
#选取好p,q后进行ARIMA预测
model = ARIMA(data_, (p,1,q) ).fit() #建立ARIMA(0, 1, 1)模型
model.summary2() #给出一份模型报告
r = model.forecast(5) #做出未来五天的预测结果
pro_r = r[0]
print('做出未来五天的预测结果:')
print(pro_r)


#添加预测值到图像上
pre_data = pd.Series(pro_r, index=['2019/03/13', '2019/03/14', '2019/03/15', '2019/03/16', '2019/03/17'], name='SS81346')
pre_data.index.name = '日期'

#绘图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(data_, 'k', label='one')
ax.plot(pre_data,'r', label='two')
ax.set_title('商品： SS81346')
ax.set_xlabel('日期')
ax.set_ylabel('销量')
ax.set_xticks(['2018/09/01', '2018/10/01', '2018/11/01',
               '2018/12/01', '2019/01/01', '2019/02/01', '2019/02/28', '2019/03/18'])
plt.show()

