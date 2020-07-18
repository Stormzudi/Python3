# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 21:15
# @Author  : ZhuNian
# @FileName: course_10_4.py
# @Software: PyCharm

'''
1.search() 与 match() 的区别
2.组的学习 (.*)
'''

import re
a = 'ABC901292478'

#search() 与 match() 相同点都是匹配到了成功后就返回。
t_1 = re.search('\d', a)  #匹配字符串中的第一个整数的位置
t_2 = re.match('\d', a) #匹配字符串的第一个字符是否为整数
print(t_1,t_2)
print(t_1.groups())

print("~~~~~~~~~~~~~~~~~~~~~~~~")

#匹配life 与 python 中的字符串；
b = 'life is short, i love python'

t_3 = re.search('life(.*)python',b)
print(t_3)
print(t_3.group(1))

#匹配life 与 python中的字符串，并且也匹配 python 与 python 中的字符串
c = 'life is short, i love python, life is short, i love python'
t_4 = re.search('life(.*)python(.*)python', c)
print(t_4)
print(t_4.group(0,1,2))