# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 13:24
# @Author  : ZhuNian
# @FileName: course_11_1.py
# @Software: PyCharm

#枚举
'''
1.枚举比较
2.枚举的注意事项
3.枚举的转换
'''

from enum import Enum

#枚举比较
class VIP(Enum):  #定义一个VIP枚举类
    YELLOW = 1  #枚举中标签 ：大写
    RED = 2
    GREEN = 3
    BLACK = 'str'

result_1 = VIP.GREEN == VIP.GREEN
# result_2 = VIP.GREEN < VIP.BLACK  #不能

print(result_1)
# print(result_2)

class VIP2(Enum):  #定义一个VIP枚举类
    YELLOW = 1  #枚举中标签 ：大写
    RED = 2
    GREEN = 3
    BLACK = 4

result_3 = VIP.GREEN == VIP2.GREEN  #不能（跨枚举类）
result_4 = VIP2.GREEN in VIP2  #判断是否在枚举类中

print(result_3) #False
print(result_4)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#3.枚举的转换

class VIP3(Enum):  #定义一个VIP枚举类
    YELLOW = 1  #枚举中标签 ：大写
    RED = 2
    GREEN = 3
    BLACK = 4

a = 3
result_5 = VIP3(a)  #将 a 的值转换成枚举类型
print(result_5)
print(type(result_5))  #  <enum 'VIP3'> 注意是 enum类

