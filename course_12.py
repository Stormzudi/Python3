# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 19:26
# @Author  : ZhuNian
# @FileName: course_12.py
# @Software: PyCharm

# 函数式编程
'''
1.匿名函数
2.三元表达式
3.map()函数
4.map()函数与 lambda 结合
'''


def add(x,y):
    return  x + y

# lambda parameter_list: expression (表达式)
# lambda 表达式
f = lambda x,y: x+y  #expression (表达式)
print(add(1,3))
print(f(1,3))




print('~~~~~~~~~~~~~~~~~~~~~`')
#三元表达式
#：条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果

#其他语言： x > y ? x: y

a = 2
b = 1
r = a if a > b else b
print(r)



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#map 类
#map 函数就是一个一一映射的关系类的运算
#map 在没有结合lambda 表达式时就 for 一样效果

result_1 = (1,3,4)
result_2 = [1,3,4]

def square(x):
    return x * x

r_1 = map(square,result_1)
r_2 = map(square,result_2)
print(r_1)
print(r_2)

print(r_1.__class__.__dict__)
print(r_2.__class__.__dict__)

print(tuple(r_1))
print(list(r_2))


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 4.map()函数与 lambda 结合
#让代码变得简洁
list_x = [1,2,3,4,5,6]
list_y = [1,2,3,4,5,6,7,8]

r = map(lambda x,y: x*x +y,list_x,list_y)  #取决于较小的那个 list_x
print(list(r))