# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 17:03
# @Author  : ZhuNian
# @FileName: course_10_zijie.py
# @Software: PyCharm

'''
1. 搜索字符串是否满足要求
2. 将字符串修改成符合要求的字符串
3. 此处用正则表达式：
'''

import re

re.findall()
re.sub()

def exchange(value):
    mached = value.group() #mached 是字符串类型
    if len(mached) == 2:
        memory = mached
        return memory

    else:
        print("你输入的不是单词,剔除重复字母后的单词为：")
        re_mached = mached[0:2]
        return re_mached


#从字符中输入一个单词str
str = input()
new_str = re.sub('a{2,9}|b{2,9}|c{2,9}|d{2,9}|e{2,9}|f{2,9}|g{2,9}|h{2,9} \
                 |i{2,9}|j{2,9}|k{2,9}|l{2,9}|m{2,9}|n{2,9}|o{2,9}|p{2,9} \
                 |q{2,9}|r{2,9}|s{2,9}|t{2,9}|u{2,9}|v{2,9}|w{2,9}|x{2,9}|y{2,9}|z{2,9}',exchange, str)
print(new_str)


