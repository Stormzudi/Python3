# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:20
# @Author  : ZhuNian
# @FileName: course_10_2.py
# @Software: PyCharm

'''
正则表达式：pattern
学习有关import re 下的其他方法
1.  re.sub() #查找并替换
2.
'''

import re


'''
第一部分：
re.sub() 的运用 
1.普通替换 == 变量,replace
2.sub(),中的第二个变量可以是函数名
'''

language = 'PythonJavaC#PHPC#PHP'
#sub(pattern, repl, string, count=0, flags=0)
r = re.sub('C#','Go',language,1)
language = language.replace('C#','Go',2)  #此时的replace 可以进行与 sub进行媲美 也算是一个简约版
print(r)
print(language)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


t = 'PythonJavaC#PHPC#PHP'
def exchange(value):
    matched = value.group()  #group()函数函数表示获取到value的值，相比，group()不能获取变量值
    matched ='[]'
    #print(matched)
    return "!!" + matched + "!!"
    # print(value)
    # value = '*'
    # return value

r = re.sub('C#', exchange, t)
print(r)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#补充 group()方法
a = "123abc456"
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))    #123
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))    #abc
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))    #456
print (re.search("([0-9]*)([a-z]*)",a).group(1))   #123,返回部分
#可以看出，正则表达式按照数字-字母-数字的顺序来获取相应字符串，那么分别就是“数字（group（1））--字母（group（2））--数字（group（3））”的对应关系，
#其中，group（0）和group（）效果相同，均为获取取得的字符串整体。

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
