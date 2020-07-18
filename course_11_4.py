# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 23:07
# @Author  : ZhuNian
# @FileName: course_11_4.py
# @Software: PyCharm

'''
1.旅行者问题：
x=0 出发，每次移动都会记录之前的步子；
下一步要在上一步的基础上移动；
x= 0 3 5 8
2.global origin  #将局部变量 origin 转变成全局变量
3.nonlocal step  #闭包中用 nonlocal 将局部变量 step 转变成全局变量
'''


#普通函数方法
#global origin #将局部变量 origin 转变成全局变量

origin = 0

def go(step):
    global origin #将局部变量 origin 转变成全局变量
    new_pos = step + origin
    origin = new_pos
    return  new_pos

print(go(3),go(5),go(8))


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#函数式编程方法
#nonlocal step  #闭包中用 nonlocal 将局部变量 step 转变成全局变量

step = 0

def count_step(step):
    def func(step_now):
        nonlocal step  #闭包中用 nonlocal 将局部变量 step 转变成全局变量
        step_now = step + step_now
        step = step_now
        return step_now
    return func


t = count_step(step)
step_1 = t(3)
print(step_1)
print(t.__closure__[0].cell_contents)  #表示记录了环境值 step = 3

step_2 = t(5)
print(step_2)
print(t.__closure__[0].cell_contents)  #表示记录了环境值 step = 8

step_3 = t(8)
print(step_3)
print(t.__closure__[0].cell_contents)  #表示记录了环境值 step = 16


print(step_1,step_2,step_3)