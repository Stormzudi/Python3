# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 16:02
# @Author  : ZhuNian
# @FileName: course_12_3.py
# @Software: PyCharm

#装饰器的运用
'''
1.普通函数
2.装饰器
3.定义一个类 求取多项式的值
'''

#在已经写好的函数内，要添加一个打印时间的功能
import time

def func_1():
    print('我是func_1')

def func_2():
    print('我是func_2')

def print_time(func):
    print(time.time())  #打印具体时间
    func()

print_time(func_1)
print_time(func_2)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

#调用
t = decorator(func_1)
print(t.__closure__)
t()  #t为函数 即为 调用函数的值t()



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#定义一个类 求取多项式的 值
#a*x^2+b*x+c

class polynomial():
    def __init__(self,a,b,c): #任何一个对象都有的特性
        self.a = a
        self.b = b
        self.c = c
    def evaluation(self,x):
        r = self.a*x^2+self.b*x+self.c
        return r

demo_1 = polynomial(1,2,3)
r = demo_1.evaluation(2)
print(r)

