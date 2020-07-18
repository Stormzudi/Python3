# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 11:57
# @Author  : ZhuNian
# @FileName: course_10.py
# @Software: PyCharm

'''
#有关正则表达式的知识
1.普通字符串的匹配方法
2.运用了 import re 后 用re.findall()的字符串的匹配方法
'''

import re

a = 'Java|Python|C++|C#|C|Java|Python|C++|C#|C'

print(a.index('Python')>-1)  #运用python 中特定的 index()函数来 寻找字符串中是否有对应的字符
print('Python' in a)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#正则表达式：(规则)
result = re.findall('Python',a)  # re.findall 返回数据的类型为：列表 result[]
print(result)

if len(result) > 0:
    print("匹配到对应的字符串")
else:
    print("并未匹配到对应的字符串")

# 打印出列表中的字符
# print(len(result))
# for x in result:
#     for y in x:
#        print(y,end=" ")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

