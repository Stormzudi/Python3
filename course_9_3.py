# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 21:04
# @Author  : ZhuNian
# @FileName: course_9_3.py
# @Software: PyCharm

'''
1.实例方法访问实例变量
2.实例方法访问类变量
'''
class Student():
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age =  age
        print(self.name)  #实例方法访问实例变量
        print(self.__dict__)  #{'age': 18, 'name': '小菊'}
        print(self.num) #此时元组中虽然没有 num 参数值，但是运行 self.num时，在实例对象中找不到num 会返回到类中去寻在 num 参数的值
        print(Student.num)
        print(self.__class__.num)  #实例对象访问类中的参数


student = Student('小菊',18)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''
实例方法访问类变量
'''
class StudentCount():
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def add_num(cls):
        cls.num +=1
        #print(cls.name) 不能访问对象中参数
        print(cls.num)



student1 = StudentCount('四小红',18)
StudentCount.add_num()  #用类调用类的方法
student2 = StudentCount('小哈',18)
StudentCount.add_num()
student3 = StudentCount('方小明',18)
StudentCount.add_num()


