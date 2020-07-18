# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 15:30
# @Author  : ZhuNian
# @FileName: course_12_2.py
# @Software: PyCharm

'''
1.filter函数的运用：要不要保留集合中的内容
2.函数式编程 VS 函数编程
'''

list_1 = [1,2,0,0,1,3]
list_2 = ['a','A','b','r','R','C','2']

r_1 = filter(lambda x: False if x == 0 else True, list_1)
r_2 = filter(lambda x: x, list_1)
r_3 = filter(lambda x: True if x>='A'and x<='Z' else False, list_2) #返回大写的值
print(list(r_1),list(r_2))
print(list(r_3))
