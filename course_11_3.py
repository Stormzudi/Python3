# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 22:54
# @Author  : ZhuNian
# @FileName: course_11_3.py
# @Software: PyCharm

'''
1.环境变量与局部变量
2.#闭包
'''

#闭包
def f1():
    a = 10  #此时 a 作为 f2()函数的环境变量
    def f2():
        a = 10 #此时 a 被认为是局部变量
        return a
    return f2

f = f1()
print(f)
print(f.__closure__)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def f1():
    a = 10  #此时 a 作为 f2()函数的环境变量
    def f2():
        #a = 10 #此时 a 被认为是局部变量
        return a
    return f2

f = f1()
print(f)
print(f.__closure__) #：用来查找是否为闭包所有的属性
print(f.__closure__[0].cell_contents)  #：取出定义的环境变量值