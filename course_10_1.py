# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 12:25
# @Author  : ZhuNian
# @FileName: course_10_1.py
# @Software: PyCharm

'''
正则表达式：(规则)
1.#字符集特性
2.#概括字符集
3.#数量词
4.#边界匹配
5.#组
6.#第三个参数的利用 re.findall('','','**') 也叫匹配模式
'''

import re
a = '0Java3Python4C++7C#9C'

result = re.findall('\d',a)  #在字符串中找到对应的数字，
result1 = re.findall('\D',a)  #在字符串中找到对应的非字符
print(result)
print(result1)



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#字符集特性
s = 'abc, adc, ahc, ajcd, sgadc, aabc, sdf,'

r = re.findall('a[d]c',s)  #会识别 sgadc 中 adc
print(r)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#概括字符集
# \d \D
# \w  其中\w 为匹配单词字符和数字  \W 为匹配非单词字符和数字
# \s  匹配空白字符 \S 匹配非空白字符

a = 'fasd%341234ahf& &899'
r1 = re.findall('\W',a)  # \W 为匹配非单词字符和数字
r2 = re.findall('\s',a)  # \s  匹配空白字符
print(r1)
print(r2)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#数量词

b = 'pytho0python2pythonn3 pythoon4pythhon'
r3 = re.findall('python', b)
print(r3)
r4 = re.findall('[a-z]{3,4}', b)
r5 = re.findall('pyth{2}on', b)
print(r4)
print(r5)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#边界匹配
qq = '1000000001'
#判断此时匹配qq的长度是否在 9-10 之间
r_qq = re.findall('^\d{9,10}$',qq)
print(r_qq)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#组
zu = 'pythonpythonpythonpython'
r_zu = re.findall('(python){2}(JS)',zu)
# r_zu = re.findall('pythonpythonpython',zu)
print(r_zu)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#第三个参数的利用 re.findall('','','**')
language = 'PythonC#\nJavaPHP'
r_language = re.findall('c#',language,re.I) #此时加上 re.I 可以部分大小写进行匹配字符串
r_language_1 = re.findall('c#.{1}', language, re.I | re.S)  #加上了re.S后可以进行 匹配". " 点后面的字符
#re.findall('c#.{1}')  表示在c#后面可以访问 " . " 所以可以访问{1} ， 表示访问c#后面一个字符包括了 \n
print(r_language)
print(r_language_1)