# -*- coding: utf-8 -*-
#@ By: ZhuNian
#@ Data: 2020.3.7
#@ file: course_3.py

'''type(a) #表示显示a的数据类型'''

#type(1) #显示整数型
#type(1.0) #显示浮点型
#type(2/2)  1.0 表示浮点型
#type(2//2)  1 表示整数型



'''python 进制的转换 10 2 8 16 进制'''

#表示2进制 在数字前加：0b 
print(0b10)
#表示8进制 在数字前加：0o 
print(0o10)
#表示16进制 在数字前加：0x 
print(0x1F)


'''如何实现进制的相互转换'''
#将10，8，16进制转换成2 进制 ：用bin()
print(bin(10))
print(bin(0o7))
print(bin(0xE))
#将2，8，16进制转换成10 进制 ：用int()
print(int(0b111))
print(int(0x1F))
#将2，10，8进制转换成16 进制 ：用hex()
print(hex(888))
print(hex(0o10))
#将2，10，16进制转换成8 进制 ：用hex()
print(oct(888))
print(oct(0b10))
print(oct(0x10))


'''其他数据类型表示'''
#bool类型 ： True(非0) , False(0)  （表示真假）
print(type(True))
print(type(False))
#(归于数字类型中)
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))





