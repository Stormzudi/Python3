# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 15:04
# @Author  : ZhuNian
# @FileName: course_6_2.py
# @Software: PyCharm

#snippet 片段
'''
三种方法：
静态方法（staticmethod），类方法（classmethod）和 实例方法
'''

#普通方法：
def foo_1(x):
    print("running foo_1(%s)"%x)

foo_1("test")


#实例方法
# -*- coding:utf-8 -*-
class A:
    def foo_2(self, x):
        print("running foo_2(%s, %s)" % (self, x))

# A.foo(x) 这样会报错
a = A()
a.foo_2("test")



#类方法（classmethod）
class B:
    class_attr = "attr"

    def __init__(self):
        pass

    @classmethod
    def class_foo(cls):
        print("running class_foo(%s)" % (cls.class_attr))

a = B()
a.class_foo()
B.class_foo()



# 静态方法（staticmethod）
a=1
log_enabled = True
class C:
    class_attr = "attr"

    def __init__(self):
        pass

    @staticmethod
    def static_foo():
        print("模块下的a的值为："+ str(a))
        if log_enabled:
            print("log is enabled")
        else:
            print("log is disabled")


C.static_foo()