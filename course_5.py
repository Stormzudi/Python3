# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 18:59
# @Author  : ZhuNian
# @FileName: course_5.py
# @Software: PyCharm


'''变量与运算符'''
#变量一定要设置的有意义
a=[1,2,3,4,5,6]
b=[1,2,3]
# 列表a乘3，然后加上列表b,最后再加上列表a
print(a*3+b+a)
#print(a-b)  列表运算中没有减法
skill=[1,3]

'''
变量名的要求：
# 字母、数字、下划线  （首字母不能是数字）
# 系统的关键字不能设置成变量名 (保留关键字)：and if
'''

a=1
b=a
a=3
print(b) #此时b的值不会改变   b：为值类型 （不可变）（int，str,tuple)

a=[1,2,3]
b=a
a[0]='a'
print(b) #此时b的值在改变  b：为引用类型 （可变）(list set dict)

#a=45
#print("a=%d\nb=%d" %(a,a))
# a='adfaf'
# print(a[4])