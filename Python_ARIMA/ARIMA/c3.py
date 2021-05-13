# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 17:06
# @Author  : Zudy
# @FileName: c3.py
'''
1.岭回归实现销量预测
'''

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge  # 通过sklearn.linermode1加载岭回归方法
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures  # 通过sklearn.preprocessing加载PolynomialFeatures用于创建多项式特征
from sklearn.model_selection import train_test_split  # 交叉验证

inputfile = 'D:/Python/Python_learning/HBUT/model_3/test_four.xlsx'
data_df = pd.read_excel(inputfile, sheet_name='Sheet2')
data = np.array(data_df)
plt.plot(data[:, 6])  # 展示销量数据信息


X = data[:, 1:3]  # X用于保存day_of_year的数据
print(X)
y = data[:, 6]  # y用于保存第维数据,
poly = PolynomialFeatures(4)  # 用于创建最高次数4次方的的多项式特征,多次试验后决定采用4次
X = poly.fit_transform(X)  # X为创建的多项式特征
train_set_X, test_set_X, train_set_y, test_set_y = train_test_split(X, y, test_size=0.3, random_state=0)
# 将所有数据划分为训练集和测试集, test_ size表示测试集的比例， random_state是随机数种子

clf = Ridge(alpha=1.0, fit_intercept=True)  # 创建岭回归实例
clf.fit(train_set_X, train_set_y)  # 调用fit函数使用训练集训练回归器
score = clf.score(test_set_X, test_set_y)  # 评价拟合值的好坏(最大值：1)
print(score)

pre_data = [[193, 7],
            [194, 7],
            [195, 7]]
pre_data = poly.fit_transform(pre_data)  # 将预测数据pre_data转换成多项式特征的值
pre_data_ = clf.predict(pre_data)
print(pre_data_)



'''
利用测试集计算回归曲线的拟合优度，clf. score返回值为0.7620拟合优度,
用于评价拟合好坏,最大为1,无最小值,当对所有输入都输出同一个值时,拟合优度为0。
'''



# 绘制拟合曲线
y_pre = clf.predict(X)  # 是调用predict函数的拟合值

fig = plt.figure()  # 定义一个图片
ax = fig.add_subplot(1, 1, 1)
ax.plot(data[:, 1], y, label='real')
ax.plot(data[:, 1], y_pre,'r', label='predict')  # 展示真实数据(蓝色)以及拟合的曲线(红色)
plt.legend(loc = 'upper left') # 设置图例的位置
props = {
    'title' : 'Traffic flow forecast',
    'xlabel' : 'Period of time',
    'ylabel' : 'Number of traffic'
}
ax.set(**props)
plt.show()

