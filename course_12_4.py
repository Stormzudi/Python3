# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 19:50
# @Author  : ZhuNian
# @FileName: course_12_4.py
# @Software: PyCharm

#装饰器

import time

#定义一个装饰器
def decorator(func):
    def wrapper(*args,**kw):  # *args[]表示动态的参数列表 ，**kw:表示可以接收关键字参数
        print(time.time())  #在每个调用装饰器的函数下都执行一次time()
        func(*args,**kw)
    return wrapper

@decorator
def func_1(x):
    print('我是func_1,我的值为：',x)

@decorator
def func_2(x,y):
    t = x + y
    print('我是func_2, %d+%d值为%d'%(x,y,t))

@decorator
def func_3(x, y, a = 5, b = 2, c = 'aaa'):
    d = str(a) + str(b) + c
    e = x + y
    print('我是func_3')
    print(c,e,d)

func_1(1)
func_2(1,2)
func_3(1,2)