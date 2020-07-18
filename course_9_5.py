# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 10:03
# @Author  : ZhuNian
# @FileName: course_9_5.py
# @Software: PyCharm


#继承
#定义了新的父类 course_9_People.py
from Python3.course_9_people import *

class Student(Human):
    # sum = 0
    #
    def __init__(self, school, name, age): #构造函数定义类对象的特征
        self.school = school
        # Human.__init__(self, name, age)  #调用父类中实例方法，需要写 self
        super(Student, self).__init__(name,age) #将名字、年龄传给父类

    def do_homework(self):
        super(Student, self).get_name()  #调用父类中的实例方法 get_name()
        super(Student, self).do_homework()  #调用父类中的实例方法 do_homework()
        print("english homework")


student1 = Student('人民路小学','石敢当',18)
print(student1.__dict__)
student1.do_homework() #如果子类中的方法与父类的方法同名，只是调用子类的 方法
# Student.do_homework('')  #此时 可以用类去调用类中的方法，要传入一个参数（self）
# print(Student.sum)
# print(student1.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()