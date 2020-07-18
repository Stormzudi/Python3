# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 12:56
# @Author  : ZhuNian
# @FileName: course_11.py
# @Software: PyCharm

#枚举：枚举的重点不在枚举类型的值，而是标签
'''
1.运用枚举
2.遍历枚举
'''

from enum import Enum

class VIP(Enum):  #定义一个VIP枚举类
    YELLOW = 1  #枚举中标签 ：大写
    RED = 2
    GREEN = 3

print(type(VIP.GREEN))
print(VIP.GREEN)         #返回枚举类型
print(VIP.GREEN.value)   #返回枚举值
print(VIP.GREEN.name)   #返回枚举值的标签
print(VIP['GREEN'])   #返回枚举类型
# VIP.GREEN.value = 4  #VIP.GREEN.value的值能修改


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#遍历枚举

for i in VIP:
    print(i,i.value)

for i in VIP.__members__.items(): #(遍历) 返回枚举中的所有 枚举类型(元组)
    print(i)

for i in VIP.__members__: #(遍历) 返回枚举中的所有 枚举 标签名称
    print(i)