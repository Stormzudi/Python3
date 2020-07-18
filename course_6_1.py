# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 14:45
# @Author  : ZhuNian
# @FileName: course_6_1.py
# @Software: PyCharm

'''
一段小程序
'''
# ACCOUNT = 'ZhuNian'
# PASSWORD = '123456'
#
# print('Please input account')
# USER_ACCOUNT = input()
#
# print('Please input password')
# USER_PASSWORD = input()
#
# if ACCOUNT == USER_ACCOUNT and PASSWORD == USER_PASSWORD:
#     print("SUCCESS")
# else:
#     print('FAIL')




# 用if pass后面用函数封装 foo
# if condition:
#     pass
#           def foo()
#           {
#           }
# else:
#     pass


#新的if else 写法 :elif
# a = input()
# print('a is'%a)
# if a == 1:
#     print('apple')
# else:
#     if a == 2:
#         print('orange')
#     else:
#         if a == 3:
#             print('banana')
#         else:
#             print('shopping')


#用elif 语句

a = input()
#此时 a 接受的是字符串 str()
print(type(a))
a = int(a) #将 a 转换成整数型

if  a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('shopping')