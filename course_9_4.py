# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 21:58
# @Author  : ZhuNian
# @FileName: course_9_4.py
# @Software: PyCharm


#成员的可见性问题：
'''
1.公开的：public
2.私有的：private
'''

class Student():
    sum = 0

    def __init__(self,name,age): #构造函数定义类对象的特征
        self.name = name
        self.age = age
        self.score = 0
        self.__height = 100
        self.__class__.sum += 1

    #标记分数的行为
    def marking(self,score,__height): #方法来实现类的行为
        if score <0:
            return "不能给同学打负分"
        self.score = score
        self.__height = __height
        print(self.__height)
        print(self.name+'同学的本次考试成绩为：'+str(score))



student1 = Student('石敢当',18)
#student2 = Student('方小明',18)
student1.marking(90,150)
student1._Student__height = 110  #强行修改了类对象中私有变量的数据 _height
print(student1.__dict__)
print(student1._Student__height)

# student1._Student__height = 70
# result = student2.marking(90)
# student2.__height = 190  #这里表示新添加的变量 并复制为 __height =190 ，并不是调用了私有变量， 这里是强行赋值 {'name': '石敢当', 'score': 90, '_Student__height': 150, '__height': 110, 'age': 18}
# print(Student.sum)

