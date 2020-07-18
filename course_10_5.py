# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 22:09
# @Author  : ZhuNian
# @FileName: course_10_5.py
# @Software: PyCharm

#JSON 的知识：
'''
1.反序列化
2.数组（JSON）
3.序列化
'''

import json

#1.反序列化
json_str = '{"name":"猪猪侠","age":18}'
str = json.loads(json_str)   #将JSON 数据类型 转换成 <dict>
print(type(str))
print(str)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#2.数组（JSON）
json_str_zu = '[{"name":"猪猪侠","age":18},{"name":"zhuzhuxia","age":18}]'
str_1 = json.loads(json_str_zu)   #将JSON 数据类型 转换成 <list>
print(type(str_1))
print(str_1)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#3.序列化
student = [{'name':'猪猪侠','age':18, 'flag':'False'},{'name':'石小乐','age':18}]
print(type(student))
json_str1 = json.dumps(student)  #将python 中的<list>类型 转换成 JSON数据类型
print(type(json_str1))
print(json_str1)

