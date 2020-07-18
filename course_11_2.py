# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 22:39
# @Author  : ZhuNian
# @FileName: course_11_2.py
# @Software: PyCharm

'''
1.@unique装饰器
2.IntEnum 整型枚举类
'''
from enum import IntEnum,unique

class VIP_1(IntEnum):  #定义一个VIP枚举类 继承 IntEnum(变量为整型)
    YELLOW = 1  #枚举中标签 ：大写
    RED = 1
    GREEN = 3
    BLACK = 4


@unique
class VIP_2(IntEnum):  #定义一个VIP枚举类 继承 IntEnum(变量为整型)
    YELLOW = 1  #枚举中标签 ：大写
    # RED = 1  #不能有相同的 值
    GREEN = 3
    BLACK = 4
