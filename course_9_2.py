# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 15:53
# @Author  : ZhuNian
# @FileName: course_9_2.py
# @Software: PyCharm

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age


student = Student('老朱',18)
print(student.name)

print(student.__dict__)  #返回student 中具体的 变量值


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

class StudentCount():
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

        print(name)
        print(age)
    def count(self):
        StudentCount.num += 1 #直接用类名访问类参数

student1=StudentCount('石小菊',18)
student1.count()
print(StudentCount.__dict__)
student2=StudentCount('汤小胖',18)
student2.count()
print(StudentCount.num)



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#另外一种计数的方法
# self.__class__.num += 1
class StudentCount():
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

        print(name)
        print(age)
    #操作类中的参数
    def count(self):
        self.__class__.num += 1  #self.num += 1 的区别
        print(self.num)

student1=StudentCount('石小菊',18)
student2=StudentCount('汤小胖',18)

student1.count()
student2.count()