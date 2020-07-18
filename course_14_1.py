# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 16:56
# @Author  : ZhuNian
# @FileName: course_14_1.py
# @Software: PyCharm

'''
1.字典来代替switch
2.列表推导式
3.dict字典内的列表推导式
4.None的运用
5.系统类的自定义函数
'''

#其他语言的switch
# switch (day)
# {
#     case 0:
#       dayName = 'Sunday'
#       break;
#     case 0:
#       dayName = 'Monday'
#       break;
#     case 0:
#       dayName = 'Tuesday'
#       break;
#     ...
#     default:
#       dayName = 'UnKnow'
#       break;
# }

print('~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~')

#字典来代替switch
switcher = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
}

data = switcher.get(4, 'Unknow') #当没有匹配到时返回默认值
print(data)

#在字典中的各关键字对应的数值为函数（返回函数类型）
def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknow'

switcher_1 = {
    0 : get_sunday(),
    1 : get_monday(),
    2 : get_tuesday()
}

data = switcher.get(1, get_default()) #当没有匹配到时返回默认值
print(data)


print('~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~')

a = [1, 2, 3, 4, 5, 6, 7]
b = [i**2 for i in a if i>=5 ] #选择i>=5的值
print(b)

a = {1, 2, 3, 4, 5, 6, 7}
b = {i**2 for i in a if i>=5 } #选择i>=5的值
print(b)


print('~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~')

#dict字典内的列表推导式
student ={
    '喜小乐': 18,
    '石敢当': 19,
    '恒小五': 20
}

b = [key for key,value in student.items()]
print(b)

b = {value:key for key,value in student.items()} #将元组中的key 与 value相互替换
print(b)

b = (key for key,value in student.items()) #元组是不可变
print(b) #返回一个 generator 的对象
#打印generator中的元素
for value in b:
   print(value)


print('~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~')
a = ''
b = False
c = []
print(a == None)
print(b == None)
print(c == None)
print(type(None))
#None: 表示不存在
#False :表示真假
def func():
    return None

a = []
a = ''
a = False
a = None
if not a: #做判空操作
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

print('~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~')


#内置函数len调用的就是对象的__len__方法，默认使用的都是object的__len__方法
class Foo:
    def __len__(self):
        return 10
a = Foo()
print(len(a))  # 10

class Test():
    # def __bool__(self):
    #     return True
    def __len__(self): #在没有定义类中系统属性的内部函数__bool__时，__len__可以代替
        return True

test = Test()
print(bool(test))
