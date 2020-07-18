# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 14:04
# @Author  : ZhuNian
# @FileName: course_8_2.py
# @Software: PyCharm

#函数调用的三种方式：
'''
1.必须参数
2.关键字参数
3.默认参数
'''



def print_student_files(name, gender='男', age=18,
                        college='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

print_student_files('鸡小萌','男',19,'人民路小学') #此时 age 参数是可以修改的


'''
注意点：
1.必须参数 要在 默认参数的前面
2.默认参数是可以修改的。
'''
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def print_student_files_1(name, gender='男', age=18,
                        college='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

print_student_files_1('鸡小萌') #此时 只需要传入一个必须参数即可成立
print_student_files_1('老朱',age=17,gender='女')  #对于关键字的传入可以不用 按照顺序输入
# print_student_files_1('老小',gender='女',17,college='光明小学')  #注意 关键字参数传递的方法 与 必须实参传入的方法 不能同时存在。

'''
注意点：
1.在实参传入参数，用关键字参数传递方法时，参数顺序可以无续
2.关键字参数传递的方法 与 必须实参传入的方法 不能同时存在。
'''