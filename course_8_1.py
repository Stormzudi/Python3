# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 16:39
# @Author  : ZhuNian
# @FileName: course_8_1.py
# @Software: PyCharm

a=['zhu','nian']


def demo(x, y):
    deme_1 = x
    demo_2 = y
    return deme_1, demo_2

b = demo(a[0],a[1]) #此时返回的 b 的类型为元组类型
print(type(b))
print(b)
print(b[0],b[1])

# 用两个变量c, d 去接收demo参数值
# 避免使用 元组b 的索引去获取参数值
c , d = demo(a[0],a[1])
print(c,d)