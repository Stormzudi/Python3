# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 16:00
# @Author  : ZhuNian
# @FileName: course_8.py
# @Software: PyCharm


#定义函数

def add(x, y):
    result = x + y
    return result

#定义名称不能同名
def print_code(code):
    print(code)


a = add(1,3)
b = print_code('Python')

print(a,b) #有输出 NONE：原因由于此时中 print_code中没有 return

