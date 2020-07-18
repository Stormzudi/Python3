# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 16:50
# @Author  : ZhuNian
# @FileName: course_10_3.py
# @Software: PyCharm

#运用函数参数列表接受函数的返回值

import re


a = 'ABC901292478'
# 将字符串中的小于5的数字换成0大于5的数字换成1
def exchange(value):
    matched = value.group()
    if int(matched) > 5:
        matched = '1'
        return matched
    else:
        matched = '0'
        return matched

print('请输入一串字符串：')
b = input()
t = re.sub('\d', exchange, b)
print('按照规则，修改后的字符串：')
print(t)


