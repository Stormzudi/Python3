# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 18:45
# @Author  : ZhuNian
# @FileName: demo1.py
# @Software: PyCharm

#coding=utf-8
#例子
items = [
    {'name':'李四','age':40},
    {'name':'张三','age':30},
    {'name':'王五','age':50},
]
#对items字典按照年龄排序
items1 = sorted(items,key=lambda i:i['age'])
print(items1)

#其中 lambda理解：lambda是一个表达式，i是一个循环变量，范围是上面的例子和下面的效果一样
# def paixu():
#     for i in items:
#         i['age']
#         print(i['age'])
#
# items1 = sorted(items,key=paixu())