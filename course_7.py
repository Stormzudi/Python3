# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 21:21
# @Author  : ZhuNian
# @FileName: course_7.py
# @Software: PyCharm

#python 中循环的思想 for()  while()


#while() 一直到满足某个条件时结束循环
#使用场景 ： 在 递归中
counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:
    print('EOF')



print('***************')



#for() 主要是用于来遍历/循环 序列或者集合、字典
a = [['apple','orange','banana','grape'],(1,2,3)]
#遍历中的每一个元素
for x in a:
   for y in x:
       print(y) #print(y,end='') 横向输出
else:
    print('frult is gone')



print('***************')



#break 与 continue
a = [1,2,3]
for x in a:
    if x == 2:
        break
    print(x)
#如过 for 循环中不是正常循环结束语句的话，不会执行 else 语句；
else:
    print('EOF')



print('***************')



b = [['apple','orange','banana','grape'],(1,2,3)]
#遍历中的每一个元素
for x in b:
   for y in x:
       if y == 'orange':
           break
       print(y) #print(y,end='') 横向输出
else:
   print('frult is gone')
#此时 会执行print('frult is gone') 原因为：break 只是跳过了【】中的循环，