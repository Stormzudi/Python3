# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 10:05
# @Author  : ZhuNian
# @FileName: course_9_people.py
# @Software: PyCharm

class Human():
    sum = 0
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('this is a parent measthod')
