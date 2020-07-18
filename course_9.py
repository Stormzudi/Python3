# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 14:25
# @Author  : ZhuNian
# @FileName: course_9.py
# @Software: PyCharm

#面向对象
age = 10
print('age='+str(age))
print(type(age))
'''
此时print(<str>),打印的时候要注意到 
将age 转换成 str()字符串类型进行输出
并且输出后，此时age类型的age 仍然是 int 类型
'''

class Student():
    name = ''
    age = 0
    def print_file(self):
        print('name:'+self.name)  #调用类中的成员变量 self.变量  或  Student.变量
        print('age:'+str(self.age))

student = Student()
student.print_file()