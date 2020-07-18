# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 20:54
# @Author  : ZhuNian
# @FileName: course_12_1.py
# @Software: PyCharm

'''
1、reduce()函数的运用
2. 旅行者问题(二维)
'''

from functools import reduce

list_x = [1,2,3,4,5,6]
list_x = ['1','2','3','4','5','6']
# reduce(function, sequence, initial=None) # initial= 初始值
r = reduce(lambda x,y:x+y ,list_x)
print(r)



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#有关旅游者的问题，二位坐标的运算
# (x,y) 上：正 ，右：正

pos = [(0,0),(-1,2),(3,-9),(2,6)]
pos_2 = [[0,0],[-1,2],[3,-9],[2,6]]
print(type(pos))
print(pos[1][0])  # 值为 -1
print(pos[0]+pos[1])  # 值为 （-1，2）

pos_last = reduce(lambda x,y:x+y, pos)
pos_last_2 = reduce(lambda x,y:x+y, pos_2)
print(pos_last)
print(pos_last_2)

